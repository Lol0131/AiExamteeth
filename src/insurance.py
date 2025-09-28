# src/insurance.py
# Mock insurance plans and pricing estimation

import random
from typing import List, Dict, Any

# Mock insurance plans
INSURANCE_PLANS = {
    "Delta Dental PPO": {
        "coverage_rate": 0.80,
        "annual_max": 1500,
        "deductible": 50
    },
    "Cigna Dental": {
        "coverage_rate": 0.70,
        "annual_max": 1000,
        "deductible": 100
    },
    "MetLife Dental": {
        "coverage_rate": 0.75,
        "annual_max": 1200,
        "deductible": 75
    },
    "Aetna Dental": {
        "coverage_rate": 0.65,
        "annual_max": 800,
        "deductible": 150
    },
    "No Insurance": {
        "coverage_rate": 0.0,
        "annual_max": 0,
        "deductible": 0
    }
}

# Mock CDT codes and pricing
CDT_CODES = {
    "D2140": {"name": "Amalgam - one surface", "price": 150},
    "D2150": {"name": "Amalgam - two surfaces", "price": 200},
    "D2160": {"name": "Amalgam - three surfaces", "price": 250},
    "D2161": {"name": "Amalgam - four or more surfaces", "price": 300},
    "D2391": {"name": "Resin-based composite - one surface", "price": 180},
    "D2392": {"name": "Resin-based composite - two surfaces", "price": 220},
    "D2393": {"name": "Resin-based composite - three surfaces", "price": 280},
    "D2394": {"name": "Resin-based composite - four or more surfaces", "price": 350}
}

def map_findings_to_cdt(findings: List[Dict]) -> List[Dict]:
    """Map detected caries to appropriate CDT codes"""
    cdt_treatments = []
    
    for finding in findings:
        tooth_id = finding["tooth_id"]
        region = finding["region"]
        conf = finding["conf"]
        
        # Simple mapping logic based on region
        if "O" in region:  # Occlusal
            if conf > 0.8:
                cdt_code = "D2161"  # Four or more surfaces
            elif conf > 0.7:
                cdt_code = "D2160"  # Three surfaces
            else:
                cdt_code = "D2150"  # Two surfaces
        else:  # Buccal/Lingual
            cdt_code = "D2140"  # One surface
        
        cdt_treatments.append({
            "tooth_id": tooth_id,
            "region": region,
            "cdt_code": cdt_code,
            "procedure_name": CDT_CODES[cdt_code]["name"],
            "billed_amount": CDT_CODES[cdt_code]["price"],
            "confidence": conf
        })
    
    return cdt_treatments

def calculate_insurance_estimate(treatments: List[Dict], plan_name: str) -> Dict[str, Any]:
    """Calculate insurance coverage and patient responsibility"""
    if plan_name not in INSURANCE_PLANS:
        plan_name = "No Insurance"
    
    plan = INSURANCE_PLANS[plan_name]
    total_billed = sum(t["billed_amount"] for t in treatments)
    
    # Apply deductible
    remaining_deductible = max(0, plan["deductible"] - random.randint(0, plan["deductible"]))
    deductible_applied = min(remaining_deductible, total_billed)
    
    # Calculate coverage
    covered_amount = (total_billed - deductible_applied) * plan["coverage_rate"]
    covered_amount = min(covered_amount, plan["annual_max"])
    
    patient_responsibility = total_billed - covered_amount
    
    return {
        "plan_name": plan_name,
        "total_billed": total_billed,
        "deductible_applied": deductible_applied,
        "insurance_covers": covered_amount,
        "patient_responsibility": patient_responsibility,
        "treatments": treatments
    }

def generate_patient_message(findings: List[Dict]) -> str:
    """Generate patient-facing message about findings"""
    if not findings:
        return "Great news! No cavities were detected in your X-ray. Your teeth look healthy!"
    
    tooth_ids = [str(f["tooth_id"]) for f in findings]
    regions = [f["region"] for f in findings]
    
    message = f"We found suspected cavities on teeth {', '.join(tooth_ids)} with surfaces {', '.join(regions)}. "
    message += "Would you like to connect your insurance to see pricing at this office?"
    
    return message

def get_available_plans() -> List[str]:
    """Get list of available insurance plans"""
    return list(INSURANCE_PLANS.keys())
