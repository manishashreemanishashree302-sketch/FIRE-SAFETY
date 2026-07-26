# Fire Safety Equipment Inspection Register

This project is a React-based web application to track and manage fire safety equipment across an institution. It was built for the SIH 2026 Internal Practical Assessment.

## Getting Started

To run this project locally, you need Node.js installed.

1. **Install Dependencies**: 
   ```bash
   npm install
   ```
2. **Run the Development Server**:
   ```bash
   npm run dev
   ```
3. Open your browser and navigate to the local URL provided by Vite (usually `http://localhost:5173`).

## Data Dictionary (`data.json`)
The application loads data from `public/data.json`.
- `record_id`: Unique identifier for the register entry.
- `equipment_id`: The physical tag ID of the equipment (e.g., `EQ-ADM-1-23`).
- `type`: Type of equipment (e.g., `Water`, `CO2`, `Dry Powder`).
- `building`: Name of the building where the equipment is located.
- `floor`: Floor number or "Ground".
- `last_inspection`: Date of the last inspection (YYYY-MM-DD format).
- `next_due`: Date when the next inspection is required (YYYY-MM-DD format).
- `status`: Current status of the equipment (`Valid`, `Expiring Soon`, `Expired`, `Unknown`).
- `remarks`: Additional notes for the maintenance officer.

## Calculation Logic

The derived figure on the **Detail View** (e.g., "30 Days Until Expiry" or "10 Days Overdue") is calculated dynamically:
1. The `next_due` string is parsed into a JavaScript `Date` object.
2. The current local date (`new Date()`) is generated, and its time component is stripped to ensure an accurate day-to-day comparison.
3. The difference in milliseconds is calculated and divided by the number of milliseconds in a day (`1000 * 60 * 60 * 24`).
4. The result is rounded up using `Math.ceil()` to give the number of whole days remaining (or overdue if negative).

## Features Implemented
- **Responsive List View**: Clean, grid-based layout that adapts to narrow phone screens. Touch targets are large (>44px) for one-handed use.
- **Search & Filter**: Real-time filtering by Equipment ID, Building, or Type, alongside a status dropdown.
- **State Management**: Fully handles Loading states (with spinner), Empty states (when search yields no results), and Error states (if data fails to load).
- **Derived Metrics**: Calculates the exact days until expiry or days overdue instantly upon opening a record.
- **Awkward Cases Handled**: Missing location fields default gracefully, and records with no physical equipment display a prominent warning banner in the detail view.
