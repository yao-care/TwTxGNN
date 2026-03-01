/**
 * TwTxGNN Drug-Drug Interaction Clinical Decision Support
 *
 * This CQL library provides DDI checking for drug repurposing candidates.
 * Based on DDInter 2.0 database with 222,391 interactions.
 *
 * @author TwTxGNN Team
 * @version 1.0.0
 * @date 2026-03-01
 */
library TwTxGNN_DDI_CDS version '1.0.0'

using FHIR version '4.0.1'

include FHIRHelpers version '4.0.1'

// Code Systems
codesystem "RxNorm": 'http://www.nlm.nih.gov/research/umls/rxnorm'
codesystem "SNOMED-CT": 'http://snomed.info/sct'
codesystem "DDInterSeverity": 'https://twtxgnn.yao.care/CodeSystem/ddi-severity'

// DDI Severity Codes
code "Major": 'major' from "DDInterSeverity" display 'Major Interaction'
code "Moderate": 'moderate' from "DDInterSeverity" display 'Moderate Interaction'
code "Minor": 'minor' from "DDInterSeverity" display 'Minor Interaction'

// Context
context Patient

/**
 * Get all active medications for the patient
 */
define "Active Medications":
  [MedicationRequest: status in { 'active', 'completed' }]
    union [MedicationStatement: status in { 'active', 'completed' }]

/**
 * Extract medication codes from active medications
 */
define "Active Medication Codes":
  flatten(
    "Active Medications" M
      return M.medication.coding
  )

/**
 * Check if patient has a specific medication
 * @param drugCode The RxNorm code to check
 */
define function HasMedication(drugCode String):
  exists(
    "Active Medication Codes" C
      where C.code = drugCode
  )

/**
 * High-priority DDI pairs that require immediate attention
 * These are curated from DDInter Major interactions
 */
define "Warfarin-NSAID Interaction":
  HasMedication('11289') // Warfarin
    and (
      HasMedication('5640') // Ibuprofen
      or HasMedication('7052') // Naproxen
      or HasMedication('1191') // Aspirin
      or HasMedication('3355') // Diclofenac
    )

define "Warfarin-NSAID Alert":
  if "Warfarin-NSAID Interaction" then
    {
      severity: 'major',
      summary: 'Warfarin + NSAID: 增加出血風險',
      detail: 'Warfarin 與 NSAIDs 併用會顯著增加胃腸道出血風險。建議：考慮替代止痛藥（如 Acetaminophen）或加上胃保護劑。',
      indicator: 'critical',
      source: 'DDInter 2.0'
    }
  else
    null

/**
 * Metformin-Contrast Media Interaction
 */
define "Metformin-Contrast Interaction":
  HasMedication('6809') // Metformin
    and (
      HasMedication('42512') // Iodixanol
      or HasMedication('35782') // Iopamidol
    )

define "Metformin-Contrast Alert":
  if "Metformin-Contrast Interaction" then
    {
      severity: 'major',
      summary: 'Metformin + 含碘顯影劑: 乳酸中毒風險',
      detail: '顯影劑可能導致急性腎損傷，增加 Metformin 引起乳酸中毒的風險。建議：檢查前 48 小時停用 Metformin。',
      indicator: 'critical',
      source: 'DDInter 2.0'
    }
  else
    null

/**
 * Colchicine-CYP3A4 Inhibitor Interaction
 * Referenced from DDI-CDS.org Colchicine DDI-CDS
 */
define "Colchicine-CYP3A4 Interaction":
  HasMedication('2683') // Colchicine
    and (
      HasMedication('1738') // Clarithromycin
      or HasMedication('83395') // Ritonavir
      or HasMedication('114979') // Cobicistat
      or HasMedication('67108') // Itraconazole
    )

define "Colchicine-CYP3A4 Alert":
  if "Colchicine-CYP3A4 Interaction" then
    {
      severity: 'major',
      summary: 'Colchicine + CYP3A4 抑制劑: 毒性風險增加',
      detail: 'CYP3A4 抑制劑會顯著增加 Colchicine 血中濃度，可能導致嚴重毒性（骨髓抑制、神經病變）。建議：降低 Colchicine 劑量或避免併用。',
      indicator: 'critical',
      source: 'DDInter 2.0, DDI-CDS.org'
    }
  else
    null

/**
 * QT Prolongation Risk - Multiple drugs
 */
define "QT Prolonging Medications":
  HasMedication('89013') // Amiodarone
    or HasMedication('8787') // Sotalol
    or HasMedication('4603') // Haloperidol
    or HasMedication('42347') // Ziprasidone
    or HasMedication('72625') // Moxifloxacin

define "Multiple QT Prolongers":
  Count(
    {"Amiodarone", "Sotalol", "Haloperidol", "Ziprasidone", "Moxifloxacin"} M
      where HasMedication(
        case M
          when "Amiodarone" then '89013'
          when "Sotalol" then '8787'
          when "Haloperidol" then '4603'
          when "Ziprasidone" then '42347'
          when "Moxifloxacin" then '72625'
          else null
        end
      )
  ) >= 2

define "QT Prolongation Alert":
  if "Multiple QT Prolongers" then
    {
      severity: 'major',
      summary: '多重 QT 延長藥物: 心律不整風險',
      detail: '同時使用多種 QT 延長藥物會增加 Torsades de Pointes 風險。建議：監測心電圖、電解質，考慮替代藥物。',
      indicator: 'critical',
      source: 'DDInter 2.0'
    }
  else
    null

/**
 * Serotonin Syndrome Risk
 */
define "Serotonergic Medications":
  HasMedication('36437') // Fluoxetine
    or HasMedication('42355') // Sertraline
    or HasMedication('72625') // Paroxetine
    or HasMedication('30125') // Tramadol
    or HasMedication('6470') // Linezolid

define "Serotonin Syndrome Risk":
  Count(
    {"SSRI", "Tramadol", "Linezolid"} M
      where (
        (M = "SSRI" and (HasMedication('36437') or HasMedication('42355') or HasMedication('72625')))
        or (M = "Tramadol" and HasMedication('30125'))
        or (M = "Linezolid" and HasMedication('6470'))
      )
  ) >= 2

define "Serotonin Syndrome Alert":
  if "Serotonin Syndrome Risk" then
    {
      severity: 'major',
      summary: '血清素症候群風險',
      detail: '多種血清素作用藥物併用可能引起血清素症候群（高熱、肌躍、意識改變）。建議：監測症狀、考慮替代藥物。',
      indicator: 'warning',
      source: 'DDInter 2.0'
    }
  else
    null

/**
 * Aggregate all DDI alerts
 */
define "All DDI Alerts":
  {
    "Warfarin-NSAID Alert",
    "Metformin-Contrast Alert",
    "Colchicine-CYP3A4 Alert",
    "QT Prolongation Alert",
    "Serotonin Syndrome Alert"
  } A
    where A is not null

/**
 * Check if there are any critical alerts
 */
define "Has Critical Alerts":
  exists("All DDI Alerts" A where A.indicator = 'critical')

/**
 * Get summary of all alerts for CDS Hooks response
 */
define "Alert Summary":
  "All DDI Alerts" A
    return {
      uuid: 'ddi-' + ToString(IndexOf("All DDI Alerts", A)),
      summary: A.summary,
      indicator: A.indicator,
      detail: A.detail,
      source: A.source
    }
