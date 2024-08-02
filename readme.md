# Shipmnts Email Scheduler API

This project provides a set of APIs to manage emails, recipients, attachments, and schedule emails. The APIs are built using Django and allow CRUD operations for email management and scheduling.

## Live URL

The live instance of this API is available at: [http://shipmnts.anshrpatel.com](http://shipmnts.anshrpatel.com)

## API Endpoints

### 1. Email CRUD

- **Endpoint**: `/api/email`
- **Description**: Provides Create, Read, Update, and Delete (CRUD) operations for emails.
- **Methods**: `GET`, `POST`, `PUT`, `DELETE`

### 2. Recipient CRUD

- **Endpoint**: `/api/recipient`
- **Description**: Provides CRUD operations for recipients.
- **Methods**: `GET`, `POST`, `PUT`, `DELETE`

### 3. Attachment CRUD

- **Endpoint**: `/api/attachment`
- **Description**: Provides CRUD operations for attachments.
- **Methods**: `GET`, `POST`, `PUT`, `DELETE`

### 4. Schedule Email

- **Endpoint**: `/api/schedule-email`
- **Description**: Schedule an email with specified recurrence (daily, weekly, monthly, quarterly).
- **Methods**: `POST`
- **Parameters**:
  - `schedule`: The recurrence schedule (values: `"daily"`, `"weekly"`, `"monthly"`, `"quarterly"`).
  - `time`: The time of day to send the email in `"HH:MM"` format.
  - `day`: The day of the week to send the email (values: `"monday"`, `"tuesday"`, `"wednesday"`, `"thursday"`, `"friday"`, `"saturday"`, `"sunday"`).
  - `date`: The day of the month to send the email in `"DD"` format.
  - `email`: The primary key (pk) of the email created earlier.

### 5. List Scheduled Emails

- **Endpoint**: `/api/scheduled-emails`
- **Description**: Lists all scheduled emails.
- **Methods**: `GET`

## Usage Instructions

### Setting Up

1. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

3. **Start the Server**:
    ```bash
    python manage.py runserver
    ```

### Creating and Scheduling Emails

1. **Create an Email**:
    - Use the `/api/email` endpoint with `POST` method to create an email.

2. **Add Recipients**:
    - Use the `/api/recipient` endpoint with `POST` method to add recipients for the email.

3. **Add Attachments**:
    - Use the `/api/attachment` endpoint with `POST` method to add attachments to the email.

4. **Schedule the Email**:
    - Use the `/api/schedule-email` endpoint with `POST` method to schedule the email. Provide the appropriate values for `schedule`, `time`, `day`, `date`, and `email` fields.

5. **List Scheduled Emails**:
    - Use the `/api/scheduled-emails` endpoint with `GET` method to list all scheduled emails.

