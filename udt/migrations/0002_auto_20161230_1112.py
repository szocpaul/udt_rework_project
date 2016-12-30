# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispatcher',
            name='slug',
        ),
        migrations.AlterField(
            model_name='dispatcher',
            name='task',
            field=models.CharField(choices=[('(CIRATS Alps&amp;Germany) Administrative Tasks / CIRATS new function testing (Jazz)', '(CIRATS Alps&amp;Germany) Administrative Tasks / CIRATS new function testing (Jazz)'), ('(CIRATS Alps&amp;Germany) Administrative Tasks / Edit Settings (Blues)', '(CIRATS Alps&amp;Germany) Administrative Tasks / Edit Settings (Blues)'), ('(CIRATS Alps&amp;Germany) Administrative Tasks / Investigation (Blues)', '(CIRATS Alps&amp;Germany) Administrative Tasks / Investigation (Blues)'), ('(CIRATS Alps&amp;Germany) Administrative Tasks / QEV/CBN (Blues)', '(CIRATS Alps&amp;Germany) Administrative Tasks / QEV/CBN (Blues)'), ('(CIRATS Alps&amp;Germany) Adminsitrative Tasks / Department Data Validation (Jazz)', '(CIRATS Alps&amp;Germany) Adminsitrative Tasks / Department Data Validation (Jazz)'), ('(CIRATS Alps&amp;Germany) APAR management / APAR Approve (Blues)', '(CIRATS Alps&amp;Germany) APAR management / APAR Approve (Blues)'), ('(CIRATS Alps&amp;Germany) APAR management / APAR Edit (Rythm)', '(CIRATS Alps&amp;Germany) APAR management / APAR Edit (Rythm)'), ('(CIRATS Alps&amp;Germany) APAR management / APAR Re-open (Rythm)', '(CIRATS Alps&amp;Germany) APAR management / APAR Re-open (Rythm)'), ('(CIRATS Alps&amp;Germany) Daily Tasks / Meeting (Rythm)', '(CIRATS Alps&amp;Germany) Daily Tasks / Meeting (Rythm)'), ('(CIRATS Alps&amp;Germany) Issue management / Issue Approve (Blues)', '(CIRATS Alps&amp;Germany) Issue management / Issue Approve (Blues)'), ('(CIRATS Alps&amp;Germany) Issue management / Issue Edit (Rythm)', '(CIRATS Alps&amp;Germany) Issue management / Issue Edit (Rythm)'), ('(CIRATS Alps&amp;Germany) Issue management / Issue Re-open (Rythm)', '(CIRATS Alps&amp;Germany) Issue management / Issue Re-open (Rythm)'), ('(CIRATS Alps&amp;Germany) Issue management / Issue Transfer (Blues)', '(CIRATS Alps&amp;Germany) Issue management / Issue Transfer (Blues)'), ('(CIRATS Alps&amp;Germany) User Support / Department Document Add requests (Rythm)', '(CIRATS Alps&amp;Germany) User Support / Department Document Add requests (Rythm)'), ('(CIRATS Alps&amp;Germany) User Support / Department Document Delete requests (Rythm)', '(CIRATS Alps&amp;Germany) User Support / Department Document Delete requests (Rythm)'), ('(CIRATS Alps&amp;Germany) User Support / Department Document Edit requests (Rythm)', '(CIRATS Alps&amp;Germany) User Support / Department Document Edit requests (Rythm)'), ('(CIRATS Alps&amp;Germany) User Support / Grant or remove access (Rythm)', '(CIRATS Alps&amp;Germany) User Support / Grant or remove access (Rythm)'), ('(CIRATS Alps&amp;Germany) User Support / Information Request (Rythm)', '(CIRATS Alps&amp;Germany) User Support / Information Request (Rythm)'), ('(CIRATS DB2) Administrative Tasks / Advisory Summary (Blues)', '(CIRATS DB2) Administrative Tasks / Advisory Summary (Blues)'), ('(CIRATS DB2) Administrative Tasks / Aging report (Blues)', '(CIRATS DB2) Administrative Tasks / Aging report (Blues)'), ('(CIRATS DB2) Administrative Tasks / CBN (Jazz)', '(CIRATS DB2) Administrative Tasks / CBN (Jazz)'), ('(CIRATS DB2) Administrative Tasks / DPP related investigation (Blues)', '(CIRATS DB2) Administrative Tasks / DPP related investigation (Blues)'), ('(CIRATS DB2) Administrative Tasks / Edit Settings Request (Jazz)', '(CIRATS DB2) Administrative Tasks / Edit Settings Request (Jazz)'), ('(CIRATS DB2) Administrative Tasks / Investigation (Blues)', '(CIRATS DB2) Administrative Tasks / Investigation (Blues)'), ('(CIRATS DB2) Administrative Tasks / Monthly report (Jazz)', '(CIRATS DB2) Administrative Tasks / Monthly report (Jazz)'), ('(CIRATS DB2) Administrative Tasks / QEV (Jazz)', '(CIRATS DB2) Administrative Tasks / QEV (Jazz)'), ('(CIRATS DB2) Administrative Tasks / Summary of Retrieve CIRATS records from archive requests (Blues)', '(CIRATS DB2) Administrative Tasks / Summary of Retrieve CIRATS records from archive requests (Blues)'), ('(CIRATS DB2) Administrative Tasks / TR update (Blues)', '(CIRATS DB2) Administrative Tasks / TR update (Blues)'), ('(CIRATS DB2) Administrative Tasks / Update Sev1 distribution list (Rythm)', '(CIRATS DB2) Administrative Tasks / Update Sev1 distribution list (Rythm)'), ('(CIRATS DB2) Administrative Tasks / Weekly TSRM report (Rythm)', '(CIRATS DB2) Administrative Tasks / Weekly TSRM report (Rythm)'), ('(CIRATS DB2) Adminsitrative Tasks / Quartely Reminders (Blues)', '(CIRATS DB2) Adminsitrative Tasks / Quartely Reminders (Blues)'), ('(CIRATS DB2) Asset Invertory Database Handling / Transfer assets (Blues)', '(CIRATS DB2) Asset Invertory Database Handling / Transfer assets (Blues)'), ('(CIRATS DB2) Daily Tasks / Host or attend call (Blues)', '(CIRATS DB2) Daily Tasks / Host or attend call (Blues)'), ('(CIRATS DB2) Daily Tasks / Meeting (Rythm)', '(CIRATS DB2) Daily Tasks / Meeting (Rythm)'), ('(CIRATS DB2) Handling service requests (Blues)', '(CIRATS DB2) Handling service requests (Blues)'), ('(CIRATS DB2) IPC management / Change (Jazz)', '(CIRATS DB2) IPC management / Change (Jazz)'), ('(CIRATS DB2) IPC Management / Handling service requests (Blues)', '(CIRATS DB2) IPC Management / Handling service requests (Blues)'), ('(CIRATS DB2) IPC management / Incident (Rythm)', '(CIRATS DB2) IPC management / Incident (Rythm)'), ('(CIRATS DB2) IPC management / Problem (Jazz)', '(CIRATS DB2) IPC management / Problem (Jazz)'), ('(CIRATS DB2) Issue Management / Approve on somebodys behalf (Rythm)', '(CIRATS DB2) Issue Management / Approve on somebodys behalf (Rythm)'), ('(CIRATS DB2) Issue Management / Modify target implementation date (Rythm)', '(CIRATS DB2) Issue Management / Modify target implementation date (Rythm)'), ('(CIRATS DB2) Issue Management / Re-open record (Rythm)', '(CIRATS DB2) Issue Management / Re-open record (Rythm)'), ('(CIRATS DB2) Issue management / Retrieve record (Rythm)', '(CIRATS DB2) Issue management / Retrieve record (Rythm)'), ('(CIRATS DB2) Issue Management / Transfer records (Rythm)', '(CIRATS DB2) Issue Management / Transfer records (Rythm)'), ('(CIRATS DB2) Issue Management / Update record (Rythm)', '(CIRATS DB2) Issue Management / Update record (Rythm)'), ('(CIRATS DB2) Migration Tasks / Education material, Wiki update (Jazz)', '(CIRATS DB2) Migration Tasks / Education material, Wiki update (Jazz)'), ('(CIRATS DB2) Migration Tasks / Mails (Blues)', '(CIRATS DB2) Migration Tasks / Mails (Blues)'), ('(CIRATS DB2) Migration Tasks / Meeting (Jazz)', '(CIRATS DB2) Migration Tasks / Meeting (Jazz)'), ('(CIRATS DB2) Migration Tasks / Sametime (Blues)', '(CIRATS DB2) Migration Tasks / Sametime (Blues)'), ('(CIRATS DB2) Patch management / Approve on somebodys behalf (Rythm)', '(CIRATS DB2) Patch management / Approve on somebodys behalf (Rythm)'), ('(CIRATS DB2) Patch Management / Check records (Blues)', '(CIRATS DB2) Patch Management / Check records (Blues)'), ('(CIRATS DB2) Patch Management / Create records (Blues)', '(CIRATS DB2) Patch Management / Create records (Blues)'), ('(CIRATS DB2) Patch management / Modify target implementation date (Rythm)', '(CIRATS DB2) Patch management / Modify target implementation date (Rythm)'), ('(CIRATS DB2) Patch management / Reopen record (Rythm)', '(CIRATS DB2) Patch management / Reopen record (Rythm)'), ('(CIRATS DB2) Patch management / Retrieve record (Rythm)', '(CIRATS DB2) Patch management / Retrieve record (Rythm)'), ('(CIRATS DB2) Patch management / Transfer records (Rythm)', '(CIRATS DB2) Patch management / Transfer records (Rythm)'), ('(CIRATS DB2) Patch management / Update record (Rythm)', '(CIRATS DB2) Patch management / Update record (Rythm)'), ('(CIRATS DB2) User Support / Account Document related requests (Rythm)', '(CIRATS DB2) User Support / Account Document related requests (Rythm)'), ('(CIRATS DB2) User Support / CIRATS Report Access (Rythm)', '(CIRATS DB2) User Support / CIRATS Report Access (Rythm)'), ('(CIRATS DB2) User Support / Cognos  (Blues)', '(CIRATS DB2) User Support / Cognos  (Blues)'), ('(CIRATS DB2) User Support / Department Document related request (Rythm)', '(CIRATS DB2) User Support / Department Document related request (Rythm)'), ('(CIRATS DB2) User Support / Group related request (Rythm)', '(CIRATS DB2) User Support / Group related request (Rythm)'), ('(CIRATS DB2) User Support / Process mail on TaskID (Rythm)', '(CIRATS DB2) User Support / Process mail on TaskID (Rythm)'), ('(CIRATS DB2) User Support / SameTime support (Rythm)', '(CIRATS DB2) User Support / SameTime support (Rythm)'), ('(CWP) Generating and maintaining report (Jazz)', '(CWP) Generating and maintaining report (Jazz)'), ('(CWP) Maintaining and administrating Database (Blues)', '(CWP) Maintaining and administrating Database (Blues)'), ('(CWP) Monitoring and maintaining user support request (Blues)', '(CWP) Monitoring and maintaining user support request (Blues)'), ('(CWP) Performing and maintaining access requests (Rythm)', '(CWP) Performing and maintaining access requests (Rythm)'), ('(CWP) Performing and maintaining CBN (Jazz)', '(CWP) Performing and maintaining CBN (Jazz)'), ('(CWP) Performing and maintaining change requests (Jazz)', '(CWP) Performing and maintaining change requests (Jazz)'), ('(CWP) Performing and maintaining mass upload (Blues)', '(CWP) Performing and maintaining mass upload (Blues)'), ('(CWP) Performing and maintaining QEV (Blues)', '(CWP) Performing and maintaining QEV (Blues)'), ('(CWP) Performing and maintaining roll-over (Jazz)', '(CWP) Performing and maintaining roll-over (Jazz)'), ('(ECM) Application issues (Blues)', '(ECM) Application issues (Blues)'), ('(ECM) Archiving (Blues)', '(ECM) Archiving (Blues)'), ('(ECM) Automated process investigation and problem solving (Jazz)', '(ECM) Automated process investigation and problem solving (Jazz)'), ('(ECM) Automatizing manual jobs (Jazz)', '(ECM) Automatizing manual jobs (Jazz)'), ('(ECM) Board new customers, modify deleting them, and related tasks (Rythm)', '(ECM) Board new customers, modify deleting them, and related tasks (Rythm)'), ('(ECM) Change Management - Completing change request (Jazz)', '(ECM) Change Management - Completing change request (Jazz)'), ('(ECM) Change Management - Open/review change request (Jazz)', '(ECM) Change Management - Open/review change request (Jazz)'), ('(ECM) Configure the tool (Jazz)', '(ECM) Configure the tool (Jazz)'), ('(ECM) Cooperating with technical support teams (Jazz)', '(ECM) Cooperating with technical support teams (Jazz)'), ('(ECM) Creating/updating documentation (Jazz)', '(ECM) Creating/updating documentation (Jazz)'), ('(ECM) Daily Healthcheck by a checklist (Blues)', '(ECM) Daily Healthcheck by a checklist (Blues)'), ('(ECM) Data Feed setup (Blues)', '(ECM) Data Feed setup (Blues)'), ('(ECM) Handle service request templates (customer status and interface administration) (Rythm)', '(ECM) Handle service request templates (customer status and interface administration) (Rythm)'), ('(ECM) Handling user access requests   (Rythm)', '(ECM) Handling user access requests   (Rythm)'), ('(ECM) Interface Administration (Rythm)', '(ECM) Interface Administration (Rythm)'), ('(ECM) Manual data feed setup, problem investigation and resolving (Jazz)', '(ECM) Manual data feed setup, problem investigation and resolving (Jazz)'), ('(ECM) Open Change request to technical teams (Blues)', '(ECM) Open Change request to technical teams (Blues)'), ('(ECM) Performing User ID revalidation (Jazz)', '(ECM) Performing User ID revalidation (Jazz)'), ('(ECM) Pilot Test (Jazz)', '(ECM) Pilot Test (Jazz)'), ('(ECM) Problem Management - handling transferred tickets (Blues)', '(ECM) Problem Management - handling transferred tickets (Blues)'), ('(ECM) Problem Management - open ticket (Rythm)', '(ECM) Problem Management - open ticket (Rythm)'), ('(ECM) Provide information about application usage (Rythm)', '(ECM) Provide information about application usage (Rythm)'), ('(ECM) Providing Reports (Blues)', '(ECM) Providing Reports (Blues)'), ('(ECM) Regression Test (Blues)', '(ECM) Regression Test (Blues)'), ('(ECM) Resolving Complex level issues (Jazz)', '(ECM) Resolving Complex level issues (Jazz)'), ('(ECM) Resolving Medium level issues (Blues)', '(ECM) Resolving Medium level issues (Blues)'), ('(ECM) Resolving Simple level issues (Rythm)', '(ECM) Resolving Simple level issues (Rythm)'), ('(ECM) Server Realignment (Blues)', '(ECM) Server Realignment (Blues)'), ('(ECM) Solving access problems (Blues)', '(ECM) Solving access problems (Blues)'), ('(ECM) Solving automated data feed requests (Blues)', '(ECM) Solving automated data feed requests (Blues)'), ('(ECM) Solving data feed problems (Blues)', '(ECM) Solving data feed problems (Blues)'), ('(ECM) Solving manual data feed requests (Blues)', '(ECM) Solving manual data feed requests (Blues)'), ('(ECM) Support Management (Jazz)', '(ECM) Support Management (Jazz)'), ('(ECM) Support URT management in decisions with technical information (Jazz)', '(ECM) Support URT management in decisions with technical information (Jazz)'), ('(ECM) Tool related meetings (Jazz)', '(ECM) Tool related meetings (Jazz)'), ('(ECM) Tool related testing activities (Jazz)', '(ECM) Tool related testing activities (Jazz)'), ('(ECM) User Acceptance Test (Blues)', '(ECM) User Acceptance Test (Blues)'), ('(ePolicy) Collaborate with other (development and policy management) teams, UAT (Blues)', '(ePolicy) Collaborate with other (development and policy management) teams, UAT (Blues)'), ('(ePolicy) Communicate with the users send notification about planned outage (Blues)', '(ePolicy) Communicate with the users send notification about planned outage (Blues)'), ('(ePolicy) Create/Update accounts. (Rythm)', '(ePolicy) Create/Update accounts. (Rythm)'), ('(ePolicy) Create/Update user access (Rythm)', '(ePolicy) Create/Update user access (Rythm)'), ('(ePolicy) Investigate and resolve problem through the web interface (Rythm)', '(ePolicy) Investigate and resolve problem through the web interface (Rythm)'), ('(ePolicy) Investigations on the web interface (to solve user related problems) (Blues)', '(ePolicy) Investigations on the web interface (to solve user related problems) (Blues)'), ('(ePolicy) Manage templates through the web interface (Rythm)', '(ePolicy) Manage templates through the web interface (Rythm)'), ('(ePolicy) Open Incident / Change ticket (Blues)', '(ePolicy) Open Incident / Change ticket (Blues)'), ('(ePolicy) Perform Change (Blues)', '(ePolicy) Perform Change (Blues)'), ('(ePolicy) Prepare and perform CBN (Blues)', '(ePolicy) Prepare and perform CBN (Blues)'), ('(ePolicy) Tool related meetings (Blues)', '(ePolicy) Tool related meetings (Blues)'), ('(ITIM) Analyze existing security environment and implement enhancements for IAM Automation Products (Jazz)', '(ITIM) Analyze existing security environment and implement enhancements for IAM Automation Products (Jazz)'), ('(ITIM) Automating BAU task via scripts (Jazz)', '(ITIM) Automating BAU task via scripts (Jazz)'), ('(ITIM) Configuring the tool (Rythm)', '(ITIM) Configuring the tool (Rythm)'), ('(ITIM) Creating / modifying workflows, policies and application profiles (Jazz)', '(ITIM) Creating / modifying workflows, policies and application profiles (Jazz)'), ('(ITIM) Investigating, fixing or providing support in client side technical problems (Blues)', '(ITIM) Investigating, fixing or providing support in client side technical problems (Blues)'), ('(ITIM) Investigating, fixing or providing support in User and User ID related issues (Blues)', '(ITIM) Investigating, fixing or providing support in User and User ID related issues (Blues)'), ('(ITIM) Performing one way confirmation (no response required) periodic continued business need revalidation for IBM employee user IDs (Blues)', '(ITIM) Performing one way confirmation (no response required) periodic continued business need revalidation for IBM employee user IDs (Blues)'), ('(ITIM) Planing, coordinating, tracking deployment of tools (Jazz)', '(ITIM) Planing, coordinating, tracking deployment of tools (Jazz)'), ('(ITIM) Provide steady state support for User ID Management Automation Product customization. (Blues)', '(ITIM) Provide steady state support for User ID Management Automation Product customization. (Blues)'), ('(ITIM) Providing information / evidences to end users, audits, reviews, KCO tests (Blues)', '(ITIM) Providing information / evidences to end users, audits, reviews, KCO tests (Blues)'), ('(ITIM) Registering sharedID (Rythm)', '(ITIM) Registering sharedID (Rythm)'), ('(ITIM) Registering system into the tool (Rythm)', '(ITIM) Registering system into the tool (Rythm)'), ('(ITIM) Removing sharedID (Rythm)', '(ITIM) Removing sharedID (Rythm)'), ('(ITIM) Removing system from the tool (Rythm)', '(ITIM) Removing system from the tool (Rythm)'), ('(ITIM) Retaining audit artifacts of privileged user ID approvals, verifications and revalidations for two years (Rythm)', '(ITIM) Retaining audit artifacts of privileged user ID approvals, verifications and revalidations for two years (Rythm)'), ('(ITIM) Setting up / creating / loading access roles structure (Blues)', '(ITIM) Setting up / creating / loading access roles structure (Blues)'), ('(ITIM) Testing, evaluating and implementing code changes (Jazz)', '(ITIM) Testing, evaluating and implementing code changes (Jazz)'), ('(ITIM) Updating / modifying solution components (Jazz)', '(ITIM) Updating / modifying solution components (Jazz)'), ('(SA&amp;D) E-mail / Sametime / call support for users (Blues)', '(SA&amp;D) E-mail / Sametime / call support for users (Blues)'), ('(SA&amp;D) Ensuring problem has been resolved by requesting closure confirmation from users (Blues)', '(SA&amp;D) Ensuring problem has been resolved by requesting closure confirmation from users (Blues)'), ('(SA&amp;D) Follow up status of the Fault Reports (User wants to know the status) (Rythm)', '(SA&amp;D) Follow up status of the Fault Reports (User wants to know the status) (Rythm)'), ('(SA&amp;D) Giving a got to go for the new Release to be implemented to production databases (Rythm)', '(SA&amp;D) Giving a got to go for the new Release to be implemented to production databases (Rythm)'), ('(SA&amp;D) Handling user access requests (Rythm)', '(SA&amp;D) Handling user access requests (Rythm)'), ('(SA&amp;D) Informing GEO/IMT Leads that a problem has been resolved and FR has been closed (Rythm)', '(SA&amp;D) Informing GEO/IMT Leads that a problem has been resolved and FR has been closed (Rythm)'), ('(SA&amp;D) Performing activities related to service activation and deactivation (SA&amp;D) process (Blues)', '(SA&amp;D) Performing activities related to service activation and deactivation (SA&amp;D) process (Blues)'), ('(SA&amp;D) Performing User ID revalidation (Rythm)', '(SA&amp;D) Performing User ID revalidation (Rythm)'), ('(SA&amp;D) Providing required audit records (Blues)', '(SA&amp;D) Providing required audit records (Blues)'), ('(SA&amp;D) Providing the list of logged changes to the GEOs before their Change Board (Rythm)', '(SA&amp;D) Providing the list of logged changes to the GEOs before their Change Board (Rythm)'), ('(SA&amp;D) Receiving list of changes from the GEO Change Board and prepare them to the Global Change Board (Rythm)', '(SA&amp;D) Receiving list of changes from the GEO Change Board and prepare them to the Global Change Board (Rythm)'), ('(SA&amp;D) Retaining audit artifacts of privileged user ID approvals, verifications and revalidations for two years (Rythm)', '(SA&amp;D) Retaining audit artifacts of privileged user ID approvals, verifications and revalidations for two years (Rythm)'), ('(SA&amp;D) Testing the new version, log bugs and follow up resolution after implementing the new Release into the test database (Blues)', '(SA&amp;D) Testing the new version, log bugs and follow up resolution after implementing the new Release into the test database (Blues)'), ('(SA&amp;D) Understanding an log Changes to the next Change Board (Blues)', '(SA&amp;D) Understanding an log Changes to the next Change Board (Blues)'), ('(SA&amp;D) Understanding and logging Incidents reported via SAD tool incident/UK/IBM (ST conversation and net meeting for further details if needed) (Blues)', '(SA&amp;D) Understanding and logging Incidents reported via SAD tool incident/UK/IBM (ST conversation and net meeting for further details if needed) (Blues)'), ('(SA&amp;D) Update the tool user guide after the new release test has been done and cleared (Rythm)', '(SA&amp;D) Update the tool user guide after the new release test has been done and cleared (Rythm)'), ('(SA&amp;D) Updating the RFCs in the Defect Tracker as per the Global Change Board decisions (Rythm)', '(SA&amp;D) Updating the RFCs in the Defect Tracker as per the Global Change Board decisions (Rythm)'), ('(SA&amp;D) Updating the wiki page for Change Board once a Change has been logged (Rythm)', '(SA&amp;D) Updating the wiki page for Change Board once a Change has been logged (Rythm)'), ('(SecInfo) Handling approver request (Rythm)', '(SecInfo) Handling approver request (Rythm)'), ('(SecInfo) Handling user access / revoke request (Rythm)', '(SecInfo) Handling user access / revoke request (Rythm)'), ('(URT) Automatizing manual jobs (Jazz)', '(URT) Automatizing manual jobs (Jazz)'), ('(URT) Change Management - Completing change request (Jazz)', '(URT) Change Management - Completing change request (Jazz)'), ('(URT) Configuring the tool (Jazz)', '(URT) Configuring the tool (Jazz)'), ('(URT) Cooperating with technical support teams (Jazz)', '(URT) Cooperating with technical support teams (Jazz)'), ('(URT) Creating/updating documentation (Jazz)', '(URT) Creating/updating documentation (Jazz)'), ('(URT) Customer definition (Rythm)', '(URT) Customer definition (Rythm)'), ('(URT) Customer related sub-activities (Rythm)', '(URT) Customer related sub-activities (Rythm)'), ('(URT) Handling user access requests (Rythm)', '(URT) Handling user access requests (Rythm)'), ('(URT) Investigate and resolve problems with software configuration (Blues)', '(URT) Investigate and resolve problems with software configuration (Blues)'), ('(URT) Perform planned regular maintenance activities (Blues)', '(URT) Perform planned regular maintenance activities (Blues)'), ('(URT) Performing User ID revalidation (Jazz)', '(URT) Performing User ID revalidation (Jazz)'), ('(URT) Provide advice to management, technical and account teams IAM Automation Products  (Blues)', '(URT) Provide advice to management, technical and account teams IAM Automation Products  (Blues)'), ('(URT) Provide concept, design, development, user acceptance/regression testing and production rollout for User ID Management Automation solution release (Blues)', '(URT) Provide concept, design, development, user acceptance/regression testing and production rollout for User ID Management Automation solution release (Blues)'), ('(URT) Provide guidance and maintain security architecture &amp; design for new applications/software/product (Blues)', '(URT) Provide guidance and maintain security architecture &amp; design for new applications/software/product (Blues)'), ('(URT) Provide steady state support for User ID Management Automation Product customization. (Blues)', '(URT) Provide steady state support for User ID Management Automation Product customization. (Blues)'), ('(URT) Provide technical support and resolve issues with software or software setup/customizations (Blues)', '(URT) Provide technical support and resolve issues with software or software setup/customizations (Blues)'), ('(URT) Provide the support for IAM Automation products for activating and deactivating services  (Blues)', '(URT) Provide the support for IAM Automation products for activating and deactivating services  (Blues)'), ('(URT) Providing unique custom report (Jazz)', '(URT) Providing unique custom report (Jazz)'), ('(URT) Resolving Complex level issues (Jazz)', '(URT) Resolving Complex level issues (Jazz)'), ('(URT) Solving data feed problems (Jazz)', '(URT) Solving data feed problems (Jazz)'), ('(URT) Support Management (Jazz)', '(URT) Support Management (Jazz)')], max_length=250),
        ),
    ]
