
# MIS Configuration System - Complete Testing Workflow

## Test Accounts
- **Admin**: username=`admin`, password=`admin123` (IT Department)
- **HOD**: username=`hod`, password=`hod123` (Finance Department)
- **User**: username=`user`, password=`user123` (HR Department)

---

## Phase 1: Admin Role Testing

### 1.1 Login & Dashboard
- [ ] Login with admin credentials
- [ ] Verify dashboard shows all statistics (total users, departments, active FY, total uploads)
- [ ] Verify all menu items are visible: Configuration, Users, Templates, MIS Upload, Reports
- [ ] Check recent activity section displays correctly

### 1.2 Configuration Master
- [ ] Navigate to Configuration Master
- [ ] **Add Company**: Create "Tech Corp" - verify success message
- [ ] **Add Department**: Create "Sales" department - verify success message
- [ ] **Edit Department**: Click Edit on "Sales", rename to "Sales & Marketing" - verify update
- [ ] **Toggle Department**: Deactivate "Sales & Marketing" - verify status changes to Inactive
- [ ] **Toggle Department**: Reactivate "Sales & Marketing" - verify status changes to Active
- [ ] **Delete Department**: Try deleting "Finance" (has users) - verify error message about associated data
- [ ] **Delete Department**: Delete "Sales & Marketing" (no users) - verify successful deletion
- [ ] **Add Financial Year**: Create "2025-2026" (Apr 1, 2025 - Mar 31, 2026) - verify success
- [ ] **Toggle FY**: Set "2025-2026" as active - verify only one FY is active at a time

### 1.3 User Management
- [ ] Navigate to User Management
- [ ] **Create User**: Add new user
  - Username: `hod2`
  - Email: `hod2@example.com`
  - Password: `hod2123`
  - Department: HR
  - Role: HOD
- [ ] Verify user appears in the existing users list
- [ ] **Duplicate Check**: Try creating user with same username - verify error message
- [ ] **Duplicate Check**: Try creating user with same email - verify error message

### 1.4 Template Management
- [ ] Navigate to Template Management
- [ ] **Upload Template**: 
  - Create a simple Excel file (.xlsx) with sample columns (Month, Revenue, Expenses)
  - Upload for Finance department
  - Verify success message and template appears in list
- [ ] **Upload Template**: Upload another template for HR department
- [ ] Verify both templates are listed with correct departments and timestamps

### 1.5 MIS Upload (Admin)
- [ ] Navigate to MIS Upload
- [ ] Check upload window message (depends on current date)
- [ ] **If upload window is OPEN (1st-10th)**:
  - [ ] Download template for Finance department
  - [ ] Fill template with sample data and save
  - [ ] Upload file:
    - Department: Finance
    - Month: Current month
    - Financial Year: 2024-2025
  - [ ] Verify validation success message
  - [ ] Check upload history shows new upload with "Validated" status
- [ ] **If upload window is CLOSED**:
  - [ ] Verify error message preventing upload
  - [ ] Note the upload window dates shown

### 1.6 Approval Queue (Admin)
- [ ] Navigate to Approval Queue
- [ ] Verify all pending/validated uploads from all departments are visible
- [ ] **Approve Upload**: Approve one upload - verify status changes to "Approved"
- [ ] **Reject Upload**: Reject one upload - verify status changes to "Rejected"
- [ ] Download and review an upload file - verify file downloads correctly

### 1.7 Reports (Admin)
- [ ] Navigate to Reports
- [ ] Verify all uploads from all departments are visible
- [ ] **Filter by Department**: Select Finance - verify only Finance uploads show
- [ ] **Filter by FY**: Select 2024-2025 - verify only that FY's uploads show
- [ ] **Filter by Status**: Select "Approved" - verify only approved uploads show
- [ ] **Download**: Click download on any upload - verify file downloads
- [ ] Clear filters - verify all uploads show again

### 1.8 Logout
- [ ] Logout from admin account
- [ ] Verify redirect to login page

---

## Phase 2: HOD Role Testing

### 2.1 Login & Dashboard
- [ ] Login with HOD credentials (hod/hod123)
- [ ] Verify dashboard shows statistics
- [ ] Verify menu shows: Dashboard, MIS Upload, Reports (NO Configuration or Users or Templates)
- [ ] Check recent activity shows department-specific uploads

### 2.2 Access Restrictions
- [ ] Try accessing `/config-master` directly in URL - verify access denied/redirect
- [ ] Try accessing `/user-management` directly in URL - verify access denied/redirect
- [ ] Try accessing `/template-management` directly in URL - verify access denied/redirect

### 2.3 MIS Upload (HOD)
- [ ] Navigate to MIS Upload
- [ ] Verify department dropdown is disabled and shows only Finance (HOD's department)
- [ ] **If upload window is OPEN**:
  - [ ] Download template for Finance department
  - [ ] Upload file for Finance department
  - [ ] Verify cannot select other departments
  - [ ] Check upload history shows only Finance department uploads
- [ ] **Try Different Department**: Inspect HTML and manually change department_id in form
  - Submit upload
  - Verify error message "You can only upload for your own department"

### 2.4 Approval Queue (HOD)
- [ ] Navigate to Approval Queue
- [ ] Verify only Finance department pending uploads are visible (not HR or IT)
- [ ] **Approve Upload**: Approve a Finance upload - verify success
- [ ] **Reject Upload**: Reject a Finance upload - verify success
- [ ] **Try Other Department**: If you modify HTML to approve another dept's upload
  - Verify error "You can only approve uploads from your department"

### 2.5 Reports (HOD)
- [ ] Navigate to Reports
- [ ] Verify ONLY Finance department uploads are visible (filtered automatically)
- [ ] Apply filters - verify they work within Finance department scope
- [ ] Download a Finance upload - verify success
- [ ] Try accessing upload from other department via URL manipulation - verify access denied

### 2.6 Logout
- [ ] Logout from HOD account

---

## Phase 3: User Role Testing

### 3.1 Login & Dashboard
- [ ] Login with User credentials (user/user123)
- [ ] Verify dashboard shows statistics
- [ ] Verify menu shows ONLY: Dashboard, Reports (NO Upload, Configuration, Users, Templates)
- [ ] Check recent activity shows HR department uploads only

### 3.2 Access Restrictions
- [ ] Try accessing `/mis-upload` directly - verify access denied
- [ ] Try accessing `/approval-queue` directly - verify access denied
- [ ] Try accessing `/config-master` directly - verify access denied
- [ ] Try accessing `/user-management` directly - verify access denied
- [ ] Try accessing `/template-management` directly - verify access denied

### 3.3 Reports (User - Read Only)
- [ ] Navigate to Reports
- [ ] Verify ONLY HR department uploads are visible
- [ ] Apply filters - verify they work within HR department scope
- [ ] Download an HR upload - verify success
- [ ] Try accessing upload from other department via URL - verify access denied

### 3.4 Logout
- [ ] Logout from User account

---

## Phase 4: Additional Testing with Second HOD

### 4.1 Second HOD Testing
- [ ] Login as hod2 (created in Phase 1.3)
- [ ] Verify dashboard and menu items (same as HOD)
- [ ] Navigate to MIS Upload
- [ ] Verify department shows HR (not Finance)
- [ ] Navigate to Approval Queue
- [ ] Verify only HR department uploads visible (not Finance)
- [ ] Navigate to Reports
- [ ] Verify only HR department uploads visible
- [ ] Logout

---

## Phase 5: Time-Based Upload Window Testing

### 5.1 Test Upload Window Logic
**Current Date Scenarios**:

#### If Today is 1st-10th of Month:
- [ ] Login as Admin/HOD
- [ ] Navigate to MIS Upload
- [ ] Verify green message: "Upload window is open (1st-10th of the month)"
- [ ] Verify current date is displayed
- [ ] Verify upload form is visible and functional
- [ ] Upload a test file - verify success

#### If Today is 11th-31st of Month:
- [ ] Login as Admin/HOD
- [ ] Navigate to MIS Upload
- [ ] Verify yellow/warning message: "Upload window closed for the current month"
- [ ] Verify upload form is hidden or disabled
- [ ] Try to submit upload via form manipulation - verify server-side validation rejects it

---

## Phase 6: Data Validation Testing

### 6.1 Excel File Validation
- [ ] Login as Admin
- [ ] Navigate to MIS Upload (during open window)
- [ ] **Test Invalid File Types**:
  - [ ] Try uploading .pdf - verify error "Only .xls or .xlsx files allowed"
  - [ ] Try uploading .txt - verify error
  - [ ] Try uploading .doc - verify error
- [ ] **Test Empty Excel**:
  - [ ] Create completely empty .xlsx file
  - [ ] Try uploading - verify validation error about empty file
- [ ] **Test Valid Excel**:
  - [ ] Upload properly formatted Excel with data
  - [ ] Verify success with validation message

### 6.2 Department/FY Validation
- [ ] Login as Admin
- [ ] Navigate to Configuration Master
- [ ] **Duplicate Department**: Try adding existing department name - verify error
- [ ] **Duplicate FY**: Try adding existing FY name - verify error
- [ ] **Invalid FY Dates**: Try creating FY with EndDate before StartDate - verify error
- [ ] **Empty Fields**: Try submitting forms with empty required fields - verify client-side validation

---

## Phase 7: Cross-Role Workflow Testing

### 7.1 Complete Upload-Approval Workflow
1. [ ] Login as Admin
2. [ ] Upload MIS file for IT department
3. [ ] Logout
4. [ ] Login as HOD (Finance dept)
5. [ ] Navigate to Approval Queue
6. [ ] Verify IT upload is NOT visible (different department)
7. [ ] Logout
8. [ ] Login as Admin again
9. [ ] Navigate to Approval Queue
10. [ ] Approve the IT upload
11. [ ] Logout
12. [ ] Login as User
13. [ ] Navigate to Reports
14. [ ] Verify cannot see IT upload (User is HR dept)
15. [ ] Logout

---

## Phase 8: UI/UX Testing

### 8.1 Responsive Design
- [ ] Test on desktop browser (full width)
- [ ] Test on tablet size (resize browser to ~768px)
- [ ] Test on mobile size (resize browser to ~375px)
- [ ] Verify all tables are scrollable horizontally
- [ ] Verify navigation menu is accessible on all sizes

### 8.2 Visual Feedback
- [ ] Verify flash messages appear for all actions
- [ ] Check success messages are green
- [ ] Check error messages are red
- [ ] Check warning messages are yellow
- [ ] Verify status badges have correct colors (Pending=yellow, Validated=green, Approved=blue, Rejected=red)

---

## Test Results Summary

**Date Tested**: _________________

**Admin Role**: ☐ Pass ☐ Fail
**HOD Role**: ☐ Pass ☐ Fail
**User Role**: ☐ Pass ☐ Fail
**Upload Window Logic**: ☐ Pass ☐ Fail
**File Validation**: ☐ Pass ☐ Fail
**Access Control**: ☐ Pass ☐ Fail

**Issues Found**: 
_______________________________________
_______________________________________
_______________________________________

**Notes**:
_______________________________________
_______________________________________
_______________________________________
