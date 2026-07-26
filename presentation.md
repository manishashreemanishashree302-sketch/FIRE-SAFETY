---
title: Fire Safety Equipment Inspection Register
author: M. MANISHA SHREE
---

# 1. The Problem

**Hidden Risks in Plain Sight**

- Fire extinguishers and safety equipment carry paper tags showing the last inspection date.
- Nobody maintains a central list of all equipment.
- **The Consequence**: Expired units are often discovered during an audit, or far worse, when one is needed during an emergency and fails.

---

# 2. The Solution

A centralized, digital register that tracks every unit's location and inspection date, automatically calculating next due dates and instantly highlighting which units are overdue or approaching expiry for the safety officer.

---

# 3. Main Screen (List & Search)

*(Screenshot of the Main Screen with list, search, and filter)*

- Clean, responsive list showing critical details at a glance.
- Real-time search by ID, Type, or Location.
- Filter by status (Valid, Expiring Soon, Expired, Unknown).
- The total record count updates instantly as filters are applied.

---

# 4. Detail View & Derived Figure

*(Screenshot of the Detail View showing the derived figure prominently)*

- Opens instantly upon tapping a record.
- **Derived Figure**: A large, color-coded banner showing exact days until expiry (or days overdue) is placed at the very top.
- The safety officer sees the most important number *first*, avoiding the need to read through a long table.

---

# 5. Calculation Logic

**How is the derived figure calculated?**

1. The `next_due` string is parsed into a JavaScript `Date` object.
2. The current local date is fetched, stripping out the time of day.
3. The difference in milliseconds between `next_due` and today is calculated.
4. It is converted to days by dividing by `(1000 * 60 * 60 * 24)` and rounded up.
5. If the result is negative, the equipment is flagged as "Overdue".

---

# 6. Handling Edge Cases & Mobile UI

- **Loading State**: Simulated network delay with a spinner (no blank screens).
- **Empty Search**: Clear message when no results match criteria.
- **Awkward Cases**: 
  - Records with missing locations gracefully show "Unknown Loc".
  - Records with no physical equipment display a prominent yellow warning banner.
- **Mobile First**: Minimum touch targets of 44px height, single-column flexbox stack for narrow screens, and status badges use icons (✅, ⚠️, ❌) rather than color alone.

---

# 7. Current Status & Future Improvements

**What works:**
- The full search, filter, and detail view flows work perfectly with the static JSON dataset.
- Calculation logic is robust.
- Fully responsive on mobile devices.

**What is unfinished / Next improvement:**
- The data is currently static (JSON). The next step would be to implement a small backend or LocalStorage solution to allow adding new records and updating inspection dates directly from the UI without editing the JSON file manually.

---

# Thank You

**M. MANISHA SHREE**
Reg: 411725205032
PSVPEC · IT · Year II
