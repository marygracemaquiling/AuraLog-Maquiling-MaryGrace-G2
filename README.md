# AuraLog – Migraine Attack Logger & Clinical Tracking System

AuraLog is a role-based web application built with Django and Supabase (PostgreSQL) that helps migraine patients log attack episodes, pain severity, symptoms, and triggers, while allowing healthcare providers to review shared clinical logs prior to consultations.

## Core Feature (Project Development 2): Migraine Attack Logger
- **Patient Capabilities:** Full CRUD (Create, Read, Update, Delete) for migraine episodes (`start_time`, `end_time`, `severity_score` 1–10, `symptoms`, `triggers`, `medication_taken`, `notes`, and doctor-sharing toggle).
- **Healthcare Provider (Doctor) Capabilities:** Read-only clinical view of patient migraine episodes marked as shared (`is_shared_with_doctor=True`).
- **Validation & Security:** Enforces authentication, role-based access control (`@role_required`), record ownership (`patient=request.user`), and form validation (preventing future start times or end times earlier than start times).

## Local Setup Instructions
1. Clone the repository:
   ```bash
   git clone [https://github.com/marygracemaquiling/AuraLog-Maquiling-MaryGrace-G2.git](https://github.com/marygracemaquiling/AuraLog-Maquiling-MaryGrace-G2.git)
   cd AuraLog-Maquiling-MaryGrace-G2