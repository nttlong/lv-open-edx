# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Float, Integer, Numeric, SmallInteger, String, Table
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class ApiAdminApiaccessconfig(Base):
    __tablename__ = 'api_admin_apiaccessconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class ApiAdminApiaccessrequest(Base):
    __tablename__ = 'api_admin_apiaccessrequest'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    status = Column(String(255), nullable=False)
    website = Column(String(200), nullable=False)
    reason = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
    company_address = Column(String(255), nullable=False)
    company_name = Column(String(255), nullable=False)
    contacted = Column(Integer, nullable=False)
    site_id = Column(Integer, nullable=False)


class ApiAdminHistoricalapiaccessrequest(Base):
    __tablename__ = 'api_admin_historicalapiaccessrequest'

    id = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    status = Column(String(255), nullable=False)
    website = Column(String(200), nullable=False)
    reason = Column(String, nullable=False)
    history_id = Column(Integer, primary_key=True)
    history_date = Column(DateTime, nullable=False)
    history_type = Column(String(1), nullable=False)
    history_user_id = Column(Integer)
    user_id = Column(Integer)
    company_address = Column(String(255), nullable=False)
    company_name = Column(String(255), nullable=False)
    contacted = Column(Integer, nullable=False)
    site_id = Column(Integer)


class AssessmentAiclassifier(Base):
    __tablename__ = 'assessment_aiclassifier'

    id = Column(Integer, primary_key=True)
    classifier_data = Column(String(100), nullable=False)
    classifier_set_id = Column(Integer, nullable=False)
    criterion_id = Column(Integer, nullable=False)


class AssessmentAiclassifierset(Base):
    __tablename__ = 'assessment_aiclassifierset'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    algorithm_id = Column(String(128), nullable=False)
    course_id = Column(String(255), nullable=False)
    item_id = Column(String(128), nullable=False)
    rubric_id = Column(Integer, nullable=False)


class AssessmentAigradingworkflow(Base):
    __tablename__ = 'assessment_aigradingworkflow'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), nullable=False)
    course_id = Column(String(255), nullable=False)
    item_id = Column(String(128), nullable=False)
    scheduled_at = Column(DateTime, nullable=False)
    completed_at = Column(DateTime)
    algorithm_id = Column(String(128), nullable=False)
    submission_uuid = Column(String(128), nullable=False)
    essay_text = Column(String, nullable=False)
    student_id = Column(String(40), nullable=False)
    assessment_id = Column(Integer)
    classifier_set_id = Column(Integer)
    rubric_id = Column(Integer, nullable=False)


class AssessmentAitrainingworkflow(Base):
    __tablename__ = 'assessment_aitrainingworkflow'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), nullable=False)
    course_id = Column(String(255), nullable=False)
    item_id = Column(String(128), nullable=False)
    scheduled_at = Column(DateTime, nullable=False)
    completed_at = Column(DateTime)
    algorithm_id = Column(String(128), nullable=False)
    classifier_set_id = Column(Integer)


class AssessmentAitrainingworkflowTrainingExamples(Base):
    __tablename__ = 'assessment_aitrainingworkflow_training_examples'

    id = Column(Integer, primary_key=True)
    aitrainingworkflow_id = Column(Integer, nullable=False)
    trainingexample_id = Column(Integer, nullable=False)


class AssessmentAssessment(Base):
    __tablename__ = 'assessment_assessment'

    id = Column(Integer, primary_key=True)
    submission_uuid = Column(String(128), nullable=False)
    scored_at = Column(DateTime, nullable=False)
    scorer_id = Column(String(40), nullable=False)
    score_type = Column(String(2), nullable=False)
    feedback = Column(String, nullable=False)
    rubric_id = Column(Integer, nullable=False)


class AssessmentAssessmentfeedback(Base):
    __tablename__ = 'assessment_assessmentfeedback'

    id = Column(Integer, primary_key=True)
    submission_uuid = Column(String(128), nullable=False)
    feedback_text = Column(String, nullable=False)


class AssessmentAssessmentfeedbackAssessments(Base):
    __tablename__ = 'assessment_assessmentfeedback_assessments'

    id = Column(Integer, primary_key=True)
    assessmentfeedback_id = Column(Integer, nullable=False)
    assessment_id = Column(Integer, nullable=False)


class AssessmentAssessmentfeedbackOptions(Base):
    __tablename__ = 'assessment_assessmentfeedback_options'

    id = Column(Integer, primary_key=True)
    assessmentfeedback_id = Column(Integer, nullable=False)
    assessmentfeedbackoption_id = Column(Integer, nullable=False)


class AssessmentAssessmentfeedbackoption(Base):
    __tablename__ = 'assessment_assessmentfeedbackoption'

    id = Column(Integer, primary_key=True)
    text = Column(String(255), nullable=False)


class AssessmentAssessmentpart(Base):
    __tablename__ = 'assessment_assessmentpart'

    id = Column(Integer, primary_key=True)
    feedback = Column(String, nullable=False)
    assessment_id = Column(Integer, nullable=False)
    criterion_id = Column(Integer, nullable=False)
    option_id = Column(Integer)


class AssessmentCriterion(Base):
    __tablename__ = 'assessment_criterion'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    label = Column(String(100), nullable=False)
    order_num = Column(Integer, nullable=False)
    prompt = Column(String, nullable=False)
    rubric_id = Column(Integer, nullable=False)


class AssessmentCriterionoption(Base):
    __tablename__ = 'assessment_criterionoption'

    id = Column(Integer, primary_key=True)
    order_num = Column(Integer, nullable=False)
    points = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    label = Column(String(100), nullable=False)
    explanation = Column(String, nullable=False)
    criterion_id = Column(Integer, nullable=False)


class AssessmentPeerworkflow(Base):
    __tablename__ = 'assessment_peerworkflow'

    id = Column(Integer, primary_key=True)
    student_id = Column(String(40), nullable=False)
    item_id = Column(String(128), nullable=False)
    course_id = Column(String(255), nullable=False)
    submission_uuid = Column(String(128), nullable=False)
    created_at = Column(DateTime, nullable=False)
    completed_at = Column(DateTime)
    grading_completed_at = Column(DateTime)
    cancelled_at = Column(DateTime)


class AssessmentPeerworkflowitem(Base):
    __tablename__ = 'assessment_peerworkflowitem'

    id = Column(Integer, primary_key=True)
    submission_uuid = Column(String(128), nullable=False)
    started_at = Column(DateTime, nullable=False)
    scored = Column(Integer, nullable=False)
    assessment_id = Column(Integer)
    author_id = Column(Integer, nullable=False)
    scorer_id = Column(Integer, nullable=False)


class AssessmentRubric(Base):
    __tablename__ = 'assessment_rubric'

    id = Column(Integer, primary_key=True)
    content_hash = Column(String(40), nullable=False)
    structure_hash = Column(String(40), nullable=False)


class AssessmentStaffworkflow(Base):
    __tablename__ = 'assessment_staffworkflow'

    id = Column(Integer, primary_key=True)
    scorer_id = Column(String(40), nullable=False)
    course_id = Column(String(255), nullable=False)
    item_id = Column(String(128), nullable=False)
    submission_uuid = Column(String(128), nullable=False)
    created_at = Column(DateTime, nullable=False)
    grading_completed_at = Column(DateTime)
    grading_started_at = Column(DateTime)
    cancelled_at = Column(DateTime)
    assessment = Column(String(128))


class AssessmentStudenttrainingworkflow(Base):
    __tablename__ = 'assessment_studenttrainingworkflow'

    id = Column(Integer, primary_key=True)
    submission_uuid = Column(String(128), nullable=False)
    student_id = Column(String(40), nullable=False)
    item_id = Column(String(128), nullable=False)
    course_id = Column(String(255), nullable=False)


class AssessmentStudenttrainingworkflowitem(Base):
    __tablename__ = 'assessment_studenttrainingworkflowitem'

    id = Column(Integer, primary_key=True)
    order_num = Column(Integer, nullable=False)
    started_at = Column(DateTime, nullable=False)
    completed_at = Column(DateTime)
    training_example_id = Column(Integer, nullable=False)
    workflow_id = Column(Integer, nullable=False)


class AssessmentTrainingexample(Base):
    __tablename__ = 'assessment_trainingexample'

    id = Column(Integer, primary_key=True)
    raw_answer = Column(String, nullable=False)
    content_hash = Column(String(40), nullable=False)
    rubric_id = Column(Integer, nullable=False)


class AssessmentTrainingexampleOptionsSelected(Base):
    __tablename__ = 'assessment_trainingexample_options_selected'

    id = Column(Integer, primary_key=True)
    trainingexample_id = Column(Integer, nullable=False)
    criterionoption_id = Column(Integer, nullable=False)


class AuthGroup(Base):
    __tablename__ = 'auth_group'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)


class AuthGroupPermissions(Base):
    __tablename__ = 'auth_group_permissions'

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=False)


class AuthPermission(Base):
    __tablename__ = 'auth_permission'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    content_type_id = Column(Integer, nullable=False)
    codename = Column(String(100), nullable=False)


class AuthRegistration(Base):
    __tablename__ = 'auth_registration'

    id = Column(Integer, primary_key=True)
    activation_key = Column(String(32), nullable=False)
    user_id = Column(Integer, nullable=False)


class AuthUser(Base):
    __tablename__ = 'auth_user'

    id = Column(Integer, primary_key=True)
    password = Column(String(128), nullable=False)
    last_login = Column(DateTime)
    is_superuser = Column(Integer, nullable=False)
    username = Column(String(30), nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(254), nullable=False)
    is_staff = Column(Integer, nullable=False)
    is_active = Column(Integer, nullable=False)
    date_joined = Column(DateTime, nullable=False)


class AuthUserGroups(Base):
    __tablename__ = 'auth_user_groups'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    group_id = Column(Integer, nullable=False)


class AuthUserUserPermissions(Base):
    __tablename__ = 'auth_user_user_permissions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=False)


class AuthUserprofile(Base):
    __tablename__ = 'auth_userprofile'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    meta = Column(String, nullable=False)
    courseware = Column(String(255), nullable=False)
    language = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    year_of_birth = Column(Integer)
    gender = Column(String(6))
    level_of_education = Column(String(6))
    mailing_address = Column(String)
    city = Column(String)
    country = Column(String(2))
    goals = Column(String)
    allow_certificate = Column(Integer, nullable=False)
    bio = Column(String(3000))
    profile_image_uploaded_at = Column(DateTime)
    user_id = Column(Integer, nullable=False)


class BadgesBadgeassertion(Base):
    __tablename__ = 'badges_badgeassertion'

    id = Column(Integer, primary_key=True)
    data = Column(String, nullable=False)
    backend = Column(String(50), nullable=False)
    image_url = Column(String(200), nullable=False)
    assertion_url = Column(String(200), nullable=False)
    modified = Column(DateTime, nullable=False)
    created = Column(DateTime, nullable=False)
    badge_class_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class BadgesBadgeclass(Base):
    __tablename__ = 'badges_badgeclass'

    id = Column(Integer, primary_key=True)
    slug = Column(String(255), nullable=False)
    issuing_component = Column(String(50), nullable=False)
    display_name = Column(String(255), nullable=False)
    course_id = Column(String(255), nullable=False)
    description = Column(String, nullable=False)
    criteria = Column(String, nullable=False)
    mode = Column(String(100), nullable=False)
    image = Column(String(100), nullable=False)


class BadgesCoursecompleteimageconfiguration(Base):
    __tablename__ = 'badges_coursecompleteimageconfiguration'

    id = Column(Integer, primary_key=True)
    mode = Column(String(125), nullable=False)
    icon = Column(String(100), nullable=False)
    default = Column(Integer, nullable=False)


class BadgesCourseeventbadgesconfiguration(Base):
    __tablename__ = 'badges_courseeventbadgesconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    courses_completed = Column(String, nullable=False)
    courses_enrolled = Column(String, nullable=False)
    course_groups = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class BlockStructure(Base):
    __tablename__ = 'block_structure'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    data_usage_key = Column(String(255), nullable=False)
    data_version = Column(String(255))
    data_edit_timestamp = Column(DateTime)
    transformers_schema_version = Column(String(255), nullable=False)
    block_structure_schema_version = Column(String(255), nullable=False)
    data = Column(String(500), nullable=False)


class BlockStructureConfig(Base):
    __tablename__ = 'block_structure_config'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    num_versions_to_keep = Column(Integer)
    cache_timeout_in_seconds = Column(Integer)
    changed_by_id = Column(Integer)


class BookmarksBookmark(Base):
    __tablename__ = 'bookmarks_bookmark'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_key = Column(String(255), nullable=False)
    usage_key = Column(String(255), nullable=False)
    path = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
    xblock_cache_id = Column(Integer, nullable=False)


class BookmarksXblockcache(Base):
    __tablename__ = 'bookmarks_xblockcache'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_key = Column(String(255), nullable=False)
    usage_key = Column(String(255), nullable=False)
    display_name = Column(String(255), nullable=False)
    paths = Column(String, nullable=False)


class BrandingBrandingapiconfig(Base):
    __tablename__ = 'branding_brandingapiconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class BrandingBrandinginfoconfig(Base):
    __tablename__ = 'branding_brandinginfoconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    configuration = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class BulkEmailBulkemailflag(Base):
    __tablename__ = 'bulk_email_bulkemailflag'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    require_course_email_auth = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


t_bulk_email_cohorttarget = Table(
    'bulk_email_cohorttarget', metadata,
    Column('target_ptr_id', Integer, primary_key=True),
    Column('cohort_id', Integer, nullable=False)
)


class BulkEmailCourseauthorization(Base):
    __tablename__ = 'bulk_email_courseauthorization'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    email_enabled = Column(Integer, nullable=False)


class BulkEmailCourseemail(Base):
    __tablename__ = 'bulk_email_courseemail'

    id = Column(Integer, primary_key=True)
    slug = Column(String(128), nullable=False)
    subject = Column(String(128), nullable=False)
    html_message = Column(String)
    text_message = Column(String)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_id = Column(String(255), nullable=False)
    to_option = Column(String(64), nullable=False)
    template_name = Column(String(255))
    from_addr = Column(String(255))
    sender_id = Column(Integer)


class BulkEmailCourseemailTargets(Base):
    __tablename__ = 'bulk_email_courseemail_targets'

    id = Column(Integer, primary_key=True)
    courseemail_id = Column(Integer, nullable=False)
    target_id = Column(Integer, nullable=False)


class BulkEmailCourseemailtemplate(Base):
    __tablename__ = 'bulk_email_courseemailtemplate'

    id = Column(Integer, primary_key=True)
    html_template = Column(String)
    plain_template = Column(String)
    name = Column(String(255))


t_bulk_email_coursemodetarget = Table(
    'bulk_email_coursemodetarget', metadata,
    Column('target_ptr_id', Integer, primary_key=True),
    Column('track_id', Integer, nullable=False)
)


class BulkEmailOptout(Base):
    __tablename__ = 'bulk_email_optout'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    user_id = Column(Integer)


class BulkEmailTarget(Base):
    __tablename__ = 'bulk_email_target'

    id = Column(Integer, primary_key=True)
    target_type = Column(String(64), nullable=False)


class CatalogCatalogintegration(Base):
    __tablename__ = 'catalog_catalogintegration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    internal_api_url = Column(String(200), nullable=False)
    cache_ttl = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)
    service_username = Column(String(100), nullable=False)
    page_size = Column(Integer, nullable=False)


class CcxCcxfieldoverride(Base):
    __tablename__ = 'ccx_ccxfieldoverride'

    id = Column(Integer, primary_key=True)
    location = Column(String(255), nullable=False)
    field = Column(String(255), nullable=False)
    value = Column(String, nullable=False)
    ccx_id = Column(Integer, nullable=False)


class CcxCustomcourseforedx(Base):
    __tablename__ = 'ccx_customcourseforedx'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    display_name = Column(String(255), nullable=False)
    coach_id = Column(Integer, nullable=False)
    structure_json = Column(String)


class CcxconCcxcon(Base):
    __tablename__ = 'ccxcon_ccxcon'

    id = Column(Integer, primary_key=True)
    url = Column(String(200), nullable=False)
    oauth_client_id = Column(String(255), nullable=False)
    oauth_client_secret = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)


class CeleryTaskmeta(Base):
    __tablename__ = 'celery_taskmeta'

    id = Column(Integer, primary_key=True)
    task_id = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False)
    result = Column(String)
    date_done = Column(DateTime, nullable=False)
    traceback = Column(String)
    hidden = Column(Integer, nullable=False)
    meta = Column(String)


class CeleryTasksetmeta(Base):
    __tablename__ = 'celery_tasksetmeta'

    id = Column(Integer, primary_key=True)
    taskset_id = Column(String(255), nullable=False)
    result = Column(String, nullable=False)
    date_done = Column(DateTime, nullable=False)
    hidden = Column(Integer, nullable=False)


class CeleryUtilsChorddata(Base):
    __tablename__ = 'celery_utils_chorddata'

    id = Column(Integer, primary_key=True)
    serialized_callback = Column(String, nullable=False)
    callback_result_id = Column(Integer, nullable=False)


class CeleryUtilsChorddataCompletedResults(Base):
    __tablename__ = 'celery_utils_chorddata_completed_results'

    id = Column(Integer, primary_key=True)
    chorddata_id = Column(Integer, nullable=False)
    taskmeta_id = Column(Integer, nullable=False)


class CeleryUtilsFailedtask(Base):
    __tablename__ = 'celery_utils_failedtask'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    task_name = Column(String(255), nullable=False)
    task_id = Column(String(255), nullable=False)
    args = Column(String, nullable=False)
    kwargs = Column(String, nullable=False)
    exc = Column(String(255), nullable=False)
    datetime_resolved = Column(DateTime)


class CertificatesCertificategenerationconfiguration(Base):
    __tablename__ = 'certificates_certificategenerationconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class CertificatesCertificategenerationcoursesetting(Base):
    __tablename__ = 'certificates_certificategenerationcoursesetting'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_key = Column(String(255), nullable=False)
    enabled = Column(Integer, nullable=False)


class CertificatesCertificategenerationhistory(Base):
    __tablename__ = 'certificates_certificategenerationhistory'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_id = Column(String(255), nullable=False)
    is_regeneration = Column(Integer, nullable=False)
    generated_by_id = Column(Integer, nullable=False)
    instructor_task_id = Column(Integer, nullable=False)


class CertificatesCertificatehtmlviewconfiguration(Base):
    __tablename__ = 'certificates_certificatehtmlviewconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    configuration = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class CertificatesCertificateinvalidation(Base):
    __tablename__ = 'certificates_certificateinvalidation'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    notes = Column(String)
    active = Column(Integer, nullable=False)
    generated_certificate_id = Column(Integer, nullable=False)
    invalidated_by_id = Column(Integer, nullable=False)


class CertificatesCertificatetemplate(Base):
    __tablename__ = 'certificates_certificatetemplate'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    template = Column(String, nullable=False)
    organization_id = Column(Integer)
    course_key = Column(String(255))
    mode = Column(String(125))
    is_active = Column(Integer, nullable=False)


class CertificatesCertificatetemplateasset(Base):
    __tablename__ = 'certificates_certificatetemplateasset'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    description = Column(String(255))
    asset = Column(String(255), nullable=False)
    asset_slug = Column(String(255))


class CertificatesCertificatewhitelist(Base):
    __tablename__ = 'certificates_certificatewhitelist'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    whitelist = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    notes = Column(String)
    user_id = Column(Integer, nullable=False)


class CertificatesExamplecertificate(Base):
    __tablename__ = 'certificates_examplecertificate'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    description = Column(String(255), nullable=False)
    uuid = Column(String(255), nullable=False)
    access_key = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    template = Column(String(255), nullable=False)
    status = Column(String(255), nullable=False)
    error_reason = Column(String)
    download_url = Column(String(255))
    example_cert_set_id = Column(Integer, nullable=False)


class CertificatesExamplecertificateset(Base):
    __tablename__ = 'certificates_examplecertificateset'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_key = Column(String(255), nullable=False)


class CertificatesGeneratedcertificate(Base):
    __tablename__ = 'certificates_generatedcertificate'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    verify_uuid = Column(String(32), nullable=False)
    download_uuid = Column(String(32), nullable=False)
    download_url = Column(String(128), nullable=False)
    grade = Column(String(5), nullable=False)
    key = Column(String(32), nullable=False)
    distinction = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    mode = Column(String(32), nullable=False)
    name = Column(String(255), nullable=False)
    created_date = Column(DateTime, nullable=False)
    modified_date = Column(DateTime, nullable=False)
    error_reason = Column(String(512), nullable=False)
    user_id = Column(Integer, nullable=False)


class CommerceCommerceconfiguration(Base):
    __tablename__ = 'commerce_commerceconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    checkout_on_ecommerce_service = Column(Integer, nullable=False)
    single_course_checkout_page = Column(String(255), nullable=False)
    changed_by_id = Column(Integer)
    cache_ttl = Column(Integer, nullable=False)
    receipt_page = Column(String(255), nullable=False)
    enable_automatic_refund_approval = Column(Integer, nullable=False)


class ContentserverCdnuseragentsconfig(Base):
    __tablename__ = 'contentserver_cdnuseragentsconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    cdn_user_agents = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class ContentserverCourseassetcachettlconfig(Base):
    __tablename__ = 'contentserver_courseassetcachettlconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    cache_ttl = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class ContentstorePushnotificationconfig(Base):
    __tablename__ = 'contentstore_pushnotificationconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class ContentstoreVideouploadconfig(Base):
    __tablename__ = 'contentstore_videouploadconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    profile_whitelist = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class CorsCsrfXdomainproxyconfiguration(Base):
    __tablename__ = 'cors_csrf_xdomainproxyconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    whitelist = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class CorsheadersCorsmodel(Base):
    __tablename__ = 'corsheaders_corsmodel'

    id = Column(Integer, primary_key=True)
    cors = Column(String(255), nullable=False)


class CourseActionStateCoursererunstate(Base):
    __tablename__ = 'course_action_state_coursererunstate'

    id = Column(Integer, primary_key=True)
    created_time = Column(DateTime, nullable=False)
    updated_time = Column(DateTime, nullable=False)
    course_key = Column(String(255), nullable=False)
    action = Column(String(100), nullable=False)
    state = Column(String(50), nullable=False)
    should_display = Column(Integer, nullable=False)
    message = Column(String(1000), nullable=False)
    source_course_key = Column(String(255), nullable=False)
    display_name = Column(String(255), nullable=False)
    created_user_id = Column(Integer)
    updated_user_id = Column(Integer)


class CourseCreatorsCoursecreator(Base):
    __tablename__ = 'course_creators_coursecreator'

    id = Column(Integer, primary_key=True)
    state_changed = Column(DateTime, nullable=False)
    state = Column(String(24), nullable=False)
    note = Column(String(512), nullable=False)
    user_id = Column(Integer, nullable=False)


class CourseGroupsCohortmembership(Base):
    __tablename__ = 'course_groups_cohortmembership'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    course_user_group_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class CourseGroupsCoursecohort(Base):
    __tablename__ = 'course_groups_coursecohort'

    id = Column(Integer, primary_key=True)
    assignment_type = Column(String(20), nullable=False)
    course_user_group_id = Column(Integer, nullable=False)


class CourseGroupsCoursecohortssettings(Base):
    __tablename__ = 'course_groups_coursecohortssettings'

    id = Column(Integer, primary_key=True)
    is_cohorted = Column(Integer, nullable=False)
    course_id = Column(String(255), nullable=False)
    cohorted_discussions = Column(String)
    always_cohort_inline_discussions = Column(Integer, nullable=False)


class CourseGroupsCourseusergroup(Base):
    __tablename__ = 'course_groups_courseusergroup'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    course_id = Column(String(255), nullable=False)
    group_type = Column(String(20), nullable=False)


class CourseGroupsCourseusergroupUsers(Base):
    __tablename__ = 'course_groups_courseusergroup_users'

    id = Column(Integer, primary_key=True)
    courseusergroup_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class CourseGroupsCourseusergrouppartitiongroup(Base):
    __tablename__ = 'course_groups_courseusergrouppartitiongroup'

    id = Column(Integer, primary_key=True)
    partition_id = Column(Integer, nullable=False)
    group_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    course_user_group_id = Column(Integer, nullable=False)


class CourseGroupsUnregisteredlearnercohortassignments(Base):
    __tablename__ = 'course_groups_unregisteredlearnercohortassignments'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    course_id = Column(String(255), nullable=False)
    course_user_group_id = Column(Integer, nullable=False)


class CourseModesCoursemode(Base):
    __tablename__ = 'course_modes_coursemode'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    mode_slug = Column(String(100), nullable=False)
    mode_display_name = Column(String(255), nullable=False)
    min_price = Column(Integer, nullable=False)
    currency = Column(String(8), nullable=False)
    expiration_datetime = Column(DateTime)
    expiration_date = Column(Date)
    suggested_prices = Column(String(255), nullable=False)
    description = Column(String)
    sku = Column(String(255))
    expiration_datetime_is_explicit = Column(Integer, nullable=False)
    bulk_sku = Column(String(255))


class CourseModesCoursemodeexpirationconfig(Base):
    __tablename__ = 'course_modes_coursemodeexpirationconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    verification_window = Column(BigInteger, nullable=False)
    changed_by_id = Column(Integer)


class CourseModesCoursemodesarchive(Base):
    __tablename__ = 'course_modes_coursemodesarchive'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    mode_slug = Column(String(100), nullable=False)
    mode_display_name = Column(String(255), nullable=False)
    min_price = Column(Integer, nullable=False)
    suggested_prices = Column(String(255), nullable=False)
    currency = Column(String(8), nullable=False)
    expiration_date = Column(Date)
    expiration_datetime = Column(DateTime)


class CourseOverviewsCourseoverview(Base):
    __tablename__ = 'course_overviews_courseoverview'

    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    version = Column(Integer, nullable=False)
    id = Column(String(255), primary_key=True)
    _location = Column(String(255), nullable=False)
    display_name = Column(String)
    display_number_with_default = Column(String, nullable=False)
    display_org_with_default = Column(String, nullable=False)
    start = Column(DateTime)
    end = Column(DateTime)
    advertised_start = Column(String)
    course_image_url = Column(String, nullable=False)
    social_sharing_url = Column(String)
    end_of_course_survey_url = Column(String)
    certificates_display_behavior = Column(String)
    certificates_show_before_end = Column(Integer, nullable=False)
    cert_html_view_enabled = Column(Integer, nullable=False)
    has_any_active_web_certificate = Column(Integer, nullable=False)
    cert_name_short = Column(String, nullable=False)
    cert_name_long = Column(String, nullable=False)
    lowest_passing_grade = Column(Numeric(5, 2))
    days_early_for_beta = Column(Float(asdecimal=True))
    mobile_available = Column(Integer, nullable=False)
    visible_to_staff_only = Column(Integer, nullable=False)
    _pre_requisite_courses_json = Column(String, nullable=False)
    enrollment_start = Column(DateTime)
    enrollment_end = Column(DateTime)
    enrollment_domain = Column(String)
    invitation_only = Column(Integer, nullable=False)
    max_student_enrollments_allowed = Column(Integer)
    announcement = Column(DateTime)
    catalog_visibility = Column(String)
    course_video_url = Column(String)
    effort = Column(String)
    short_description = Column(String)
    org = Column(String, nullable=False)
    self_paced = Column(Integer, nullable=False)
    marketing_url = Column(String)
    eligible_for_financial_aid = Column(Integer, nullable=False)
    language = Column(String)


class CourseOverviewsCourseoverviewimageconfig(Base):
    __tablename__ = 'course_overviews_courseoverviewimageconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    small_width = Column(Integer, nullable=False)
    small_height = Column(Integer, nullable=False)
    large_width = Column(Integer, nullable=False)
    large_height = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class CourseOverviewsCourseoverviewimageset(Base):
    __tablename__ = 'course_overviews_courseoverviewimageset'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    small_url = Column(String, nullable=False)
    large_url = Column(String, nullable=False)
    course_overview_id = Column(String(255), nullable=False)


class CourseOverviewsCourseoverviewtab(Base):
    __tablename__ = 'course_overviews_courseoverviewtab'

    id = Column(Integer, primary_key=True)
    tab_id = Column(String(50), nullable=False)
    course_overview_id = Column(String(255), nullable=False)


class CourseStructuresCoursestructure(Base):
    __tablename__ = 'course_structures_coursestructure'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_id = Column(String(255), nullable=False)
    structure_json = Column(String)
    discussion_id_map_json = Column(String)


class CoursewareOfflinecomputedgrade(Base):
    __tablename__ = 'courseware_offlinecomputedgrade'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    created = Column(DateTime)
    updated = Column(DateTime, nullable=False)
    gradeset = Column(String)
    user_id = Column(Integer, nullable=False)


class CoursewareOfflinecomputedgradelog(Base):
    __tablename__ = 'courseware_offlinecomputedgradelog'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    created = Column(DateTime)
    seconds = Column(Integer, nullable=False)
    nstudents = Column(Integer, nullable=False)


class CoursewareStudentfieldoverride(Base):
    __tablename__ = 'courseware_studentfieldoverride'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_id = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    field = Column(String(255), nullable=False)
    value = Column(String, nullable=False)
    student_id = Column(Integer, nullable=False)


class CoursewareStudentmodule(Base):
    __tablename__ = 'courseware_studentmodule'

    id = Column(Integer, primary_key=True)
    module_type = Column(String(32), nullable=False)
    module_id = Column(String(255), nullable=False)
    course_id = Column(String(255), nullable=False)
    state = Column(String)
    grade = Column(Float(asdecimal=True))
    max_grade = Column(Float(asdecimal=True))
    done = Column(String(8), nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    student_id = Column(Integer, nullable=False)


class CoursewareStudentmodulehistory(Base):
    __tablename__ = 'courseware_studentmodulehistory'

    id = Column(Integer, primary_key=True)
    version = Column(String(255))
    created = Column(DateTime, nullable=False)
    state = Column(String)
    grade = Column(Float(asdecimal=True))
    max_grade = Column(Float(asdecimal=True))
    student_module_id = Column(Integer, nullable=False)


class CoursewareXmodulestudentinfofield(Base):
    __tablename__ = 'courseware_xmodulestudentinfofield'

    id = Column(Integer, primary_key=True)
    field_name = Column(String(64), nullable=False)
    value = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    student_id = Column(Integer, nullable=False)


class CoursewareXmodulestudentprefsfield(Base):
    __tablename__ = 'courseware_xmodulestudentprefsfield'

    id = Column(Integer, primary_key=True)
    field_name = Column(String(64), nullable=False)
    value = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    module_type = Column(String(64), nullable=False)
    student_id = Column(Integer, nullable=False)


class CoursewareXmoduleuserstatesummaryfield(Base):
    __tablename__ = 'courseware_xmoduleuserstatesummaryfield'

    id = Column(Integer, primary_key=True)
    field_name = Column(String(64), nullable=False)
    value = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    usage_id = Column(String(255), nullable=False)


class CrawlersCrawlersconfig(Base):
    __tablename__ = 'crawlers_crawlersconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    known_user_agents = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class CredentialsCredentialsapiconfig(Base):
    __tablename__ = 'credentials_credentialsapiconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    internal_service_url = Column(String(200), nullable=False)
    public_service_url = Column(String(200), nullable=False)
    enable_learner_issuance = Column(Integer, nullable=False)
    enable_studio_authoring = Column(Integer, nullable=False)
    cache_ttl = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class CreditCreditconfig(Base):
    __tablename__ = 'credit_creditconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    cache_ttl = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class CreditCreditcourse(Base):
    __tablename__ = 'credit_creditcourse'

    id = Column(Integer, primary_key=True)
    course_key = Column(String(255), nullable=False)
    enabled = Column(Integer, nullable=False)


class CreditCrediteligibility(Base):
    __tablename__ = 'credit_crediteligibility'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    username = Column(String(255), nullable=False)
    deadline = Column(DateTime, nullable=False)
    course_id = Column(Integer, nullable=False)


class CreditCreditprovider(Base):
    __tablename__ = 'credit_creditprovider'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    provider_id = Column(String(255), nullable=False)
    active = Column(Integer, nullable=False)
    display_name = Column(String(255), nullable=False)
    enable_integration = Column(Integer, nullable=False)
    provider_url = Column(String(200), nullable=False)
    provider_status_url = Column(String(200), nullable=False)
    provider_description = Column(String, nullable=False)
    fulfillment_instructions = Column(String)
    eligibility_email_message = Column(String, nullable=False)
    receipt_email_message = Column(String, nullable=False)
    thumbnail_url = Column(String(255), nullable=False)


class CreditCreditrequest(Base):
    __tablename__ = 'credit_creditrequest'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    uuid = Column(String(32), nullable=False)
    username = Column(String(255), nullable=False)
    parameters = Column(String, nullable=False)
    status = Column(String(255), nullable=False)
    course_id = Column(Integer, nullable=False)
    provider_id = Column(Integer, nullable=False)


class CreditCreditrequirement(Base):
    __tablename__ = 'credit_creditrequirement'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    namespace = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    display_name = Column(String(255), nullable=False)
    order = Column(Integer, nullable=False)
    criteria = Column(String, nullable=False)
    active = Column(Integer, nullable=False)
    course_id = Column(Integer, nullable=False)


class CreditCreditrequirementstatus(Base):
    __tablename__ = 'credit_creditrequirementstatus'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    username = Column(String(255), nullable=False)
    status = Column(String(32), nullable=False)
    reason = Column(String, nullable=False)
    requirement_id = Column(Integer, nullable=False)


class CreditHistoricalcreditrequest(Base):
    __tablename__ = 'credit_historicalcreditrequest'

    id = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    uuid = Column(String(32), nullable=False)
    username = Column(String(255), nullable=False)
    parameters = Column(String, nullable=False)
    status = Column(String(255), nullable=False)
    history_id = Column(Integer, primary_key=True)
    history_date = Column(DateTime, nullable=False)
    history_type = Column(String(1), nullable=False)
    course_id = Column(Integer)
    history_user_id = Column(Integer)
    provider_id = Column(Integer)


class CreditHistoricalcreditrequirementstatus(Base):
    __tablename__ = 'credit_historicalcreditrequirementstatus'

    id = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    username = Column(String(255), nullable=False)
    status = Column(String(32), nullable=False)
    reason = Column(String, nullable=False)
    history_id = Column(Integer, primary_key=True)
    history_date = Column(DateTime, nullable=False)
    history_type = Column(String(1), nullable=False)
    history_user_id = Column(Integer)
    requirement_id = Column(Integer)


class DarkLangDarklangconfig(Base):
    __tablename__ = 'dark_lang_darklangconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    released_languages = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class DjangoAdminLog(Base):
    __tablename__ = 'django_admin_log'

    id = Column(Integer, primary_key=True)
    action_time = Column(DateTime, nullable=False)
    object_id = Column(String)
    object_repr = Column(String(200), nullable=False)
    action_flag = Column(SmallInteger, nullable=False)
    change_message = Column(String, nullable=False)
    content_type_id = Column(Integer)
    user_id = Column(Integer, nullable=False)


class DjangoCommentClientPermission(Base):
    __tablename__ = 'django_comment_client_permission'

    name = Column(String(30), primary_key=True)


class DjangoCommentClientPermissionRoles(Base):
    __tablename__ = 'django_comment_client_permission_roles'

    id = Column(Integer, primary_key=True)
    permission_id = Column(String(30), nullable=False)
    role_id = Column(Integer, nullable=False)


class DjangoCommentClientRole(Base):
    __tablename__ = 'django_comment_client_role'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    course_id = Column(String(255), nullable=False)


class DjangoCommentClientRoleUsers(Base):
    __tablename__ = 'django_comment_client_role_users'

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class DjangoCommentCommonCoursediscussionsettings(Base):
    __tablename__ = 'django_comment_common_coursediscussionsettings'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    always_divide_inline_discussions = Column(Integer, nullable=False)
    divided_discussions = Column(String)
    division_scheme = Column(String(20), nullable=False)


class DjangoCommentCommonForumsconfig(Base):
    __tablename__ = 'django_comment_common_forumsconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    connection_timeout = Column(Float(asdecimal=True), nullable=False)
    changed_by_id = Column(Integer)


class DjangoContentType(Base):
    __tablename__ = 'django_content_type'

    id = Column(Integer, primary_key=True)
    app_label = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)


class DjangoMigrations(Base):
    __tablename__ = 'django_migrations'

    id = Column(Integer, primary_key=True)
    app = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    applied = Column(DateTime, nullable=False)


class DjangoOpenidAuthAssociation(Base):
    __tablename__ = 'django_openid_auth_association'

    id = Column(Integer, primary_key=True)
    server_url = Column(String, nullable=False)
    handle = Column(String(255), nullable=False)
    secret = Column(String, nullable=False)
    issued = Column(Integer, nullable=False)
    lifetime = Column(Integer, nullable=False)
    assoc_type = Column(String, nullable=False)


class DjangoOpenidAuthNonce(Base):
    __tablename__ = 'django_openid_auth_nonce'

    id = Column(Integer, primary_key=True)
    server_url = Column(String(2047), nullable=False)
    timestamp = Column(Integer, nullable=False)
    salt = Column(String(40), nullable=False)


class DjangoOpenidAuthUseropenid(Base):
    __tablename__ = 'django_openid_auth_useropenid'

    id = Column(Integer, primary_key=True)
    claimed_id = Column(String, nullable=False)
    display_id = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)


class DjangoRedirect(Base):
    __tablename__ = 'django_redirect'

    id = Column(Integer, primary_key=True)
    site_id = Column(Integer, nullable=False)
    old_path = Column(String(200), nullable=False)
    new_path = Column(String(200), nullable=False)


class DjangoSession(Base):
    __tablename__ = 'django_session'

    session_key = Column(String(40), primary_key=True)
    session_data = Column(String, nullable=False)
    expire_date = Column(DateTime, nullable=False)


class DjangoSite(Base):
    __tablename__ = 'django_site'

    id = Column(Integer, primary_key=True)
    domain = Column(String(100), nullable=False)
    name = Column(String(50), nullable=False)


class DjceleryCrontabschedule(Base):
    __tablename__ = 'djcelery_crontabschedule'

    id = Column(Integer, primary_key=True)
    minute = Column(String(64), nullable=False)
    hour = Column(String(64), nullable=False)
    day_of_week = Column(String(64), nullable=False)
    day_of_month = Column(String(64), nullable=False)
    month_of_year = Column(String(64), nullable=False)


class DjceleryIntervalschedule(Base):
    __tablename__ = 'djcelery_intervalschedule'

    id = Column(Integer, primary_key=True)
    every = Column(Integer, nullable=False)
    period = Column(String(24), nullable=False)


class DjceleryPeriodictask(Base):
    __tablename__ = 'djcelery_periodictask'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    task = Column(String(200), nullable=False)
    args = Column(String, nullable=False)
    kwargs = Column(String, nullable=False)
    queue = Column(String(200))
    exchange = Column(String(200))
    routing_key = Column(String(200))
    expires = Column(DateTime)
    enabled = Column(Integer, nullable=False)
    last_run_at = Column(DateTime)
    total_run_count = Column(Integer, nullable=False)
    date_changed = Column(DateTime, nullable=False)
    description = Column(String, nullable=False)
    crontab_id = Column(Integer)
    interval_id = Column(Integer)


class DjceleryPeriodictasks(Base):
    __tablename__ = 'djcelery_periodictasks'

    ident = Column(SmallInteger, primary_key=True)
    last_update = Column(DateTime, nullable=False)


class DjceleryTaskstate(Base):
    __tablename__ = 'djcelery_taskstate'

    id = Column(Integer, primary_key=True)
    state = Column(String(64), nullable=False)
    task_id = Column(String(36), nullable=False)
    name = Column(String(200))
    tstamp = Column(DateTime, nullable=False)
    args = Column(String)
    kwargs = Column(String)
    eta = Column(DateTime)
    expires = Column(DateTime)
    result = Column(String)
    traceback = Column(String)
    runtime = Column(Float(asdecimal=True))
    retries = Column(Integer, nullable=False)
    hidden = Column(Integer, nullable=False)
    worker_id = Column(Integer)


class DjceleryWorkerstate(Base):
    __tablename__ = 'djcelery_workerstate'

    id = Column(Integer, primary_key=True)
    hostname = Column(String(255), nullable=False)
    last_heartbeat = Column(DateTime)


class EdxvalCoursevideo(Base):
    __tablename__ = 'edxval_coursevideo'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    video_id = Column(Integer, nullable=False)
    is_hidden = Column(Integer, nullable=False)


class EdxvalEncodedvideo(Base):
    __tablename__ = 'edxval_encodedvideo'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    url = Column(String(200), nullable=False)
    file_size = Column(Integer, nullable=False)
    bitrate = Column(Integer, nullable=False)
    profile_id = Column(Integer, nullable=False)
    video_id = Column(Integer, nullable=False)


class EdxvalProfile(Base):
    __tablename__ = 'edxval_profile'

    id = Column(Integer, primary_key=True)
    profile_name = Column(String(50), nullable=False)


class EdxvalSubtitle(Base):
    __tablename__ = 'edxval_subtitle'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    fmt = Column(String(20), nullable=False)
    language = Column(String(8), nullable=False)
    content = Column(String, nullable=False)
    video_id = Column(Integer, nullable=False)


class EdxvalVideo(Base):
    __tablename__ = 'edxval_video'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    edx_video_id = Column(String(100), nullable=False)
    client_video_id = Column(String(255), nullable=False)
    duration = Column(Float(asdecimal=True), nullable=False)
    status = Column(String(255), nullable=False)


class EmailMarketingEmailmarketingconfiguration(Base):
    __tablename__ = 'email_marketing_emailmarketingconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    sailthru_key = Column(String(32), nullable=False)
    sailthru_secret = Column(String(32), nullable=False)
    sailthru_new_user_list = Column(String(48), nullable=False)
    sailthru_retry_interval = Column(Integer, nullable=False)
    sailthru_max_retries = Column(Integer, nullable=False)
    sailthru_activation_template = Column(String(20), nullable=False)
    changed_by_id = Column(Integer)
    sailthru_abandoned_cart_delay = Column(Integer, nullable=False)
    sailthru_abandoned_cart_template = Column(String(20), nullable=False)
    sailthru_content_cache_age = Column(Integer, nullable=False)
    sailthru_enroll_cost = Column(Integer, nullable=False)
    sailthru_enroll_template = Column(String(20), nullable=False)
    sailthru_get_tags_from_sailthru = Column(Integer, nullable=False)
    sailthru_purchase_template = Column(String(20), nullable=False)
    sailthru_upgrade_template = Column(String(20), nullable=False)
    sailthru_lms_url_override = Column(String(80), nullable=False)
    welcome_email_send_delay = Column(Integer, nullable=False)


class EmbargoCountry(Base):
    __tablename__ = 'embargo_country'

    id = Column(Integer, primary_key=True)
    country = Column(String(2), nullable=False)


class EmbargoCountryaccessrule(Base):
    __tablename__ = 'embargo_countryaccessrule'

    id = Column(Integer, primary_key=True)
    rule_type = Column(String(255), nullable=False)
    country_id = Column(Integer, nullable=False)
    restricted_course_id = Column(Integer, nullable=False)


class EmbargoCourseaccessrulehistory(Base):
    __tablename__ = 'embargo_courseaccessrulehistory'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    course_key = Column(String(255), nullable=False)
    snapshot = Column(String)


class EmbargoEmbargoedcourse(Base):
    __tablename__ = 'embargo_embargoedcourse'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    embargoed = Column(Integer, nullable=False)


class EmbargoEmbargoedstate(Base):
    __tablename__ = 'embargo_embargoedstate'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    embargoed_countries = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class EmbargoIpfilter(Base):
    __tablename__ = 'embargo_ipfilter'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    whitelist = Column(String, nullable=False)
    blacklist = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class EmbargoRestrictedcourse(Base):
    __tablename__ = 'embargo_restrictedcourse'

    id = Column(Integer, primary_key=True)
    course_key = Column(String(255), nullable=False)
    enroll_msg_key = Column(String(255), nullable=False)
    access_msg_key = Column(String(255), nullable=False)
    disable_access_check = Column(Integer, nullable=False)


class EnterpriseEnrollmentnotificationemailtemplate(Base):
    __tablename__ = 'enterprise_enrollmentnotificationemailtemplate'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    plaintext_template = Column(String, nullable=False)
    html_template = Column(String, nullable=False)
    subject_line = Column(String(100), nullable=False)
    site_id = Column(Integer, nullable=False)


class EnterpriseEnterprisecourseenrollment(Base):
    __tablename__ = 'enterprise_enterprisecourseenrollment'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    consent_granted = Column(Integer)
    course_id = Column(String(255), nullable=False)
    enterprise_customer_user_id = Column(Integer, nullable=False)


class EnterpriseEnterprisecustomer(Base):
    __tablename__ = 'enterprise_enterprisecustomer'

    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    uuid = Column(String(32), primary_key=True)
    name = Column(String(255), nullable=False)
    active = Column(Integer, nullable=False)
    site_id = Column(Integer, nullable=False)
    catalog = Column(Integer)
    enable_data_sharing_consent = Column(Integer, nullable=False)
    enforce_data_sharing_consent = Column(String(25), nullable=False)
    enable_audit_enrollment = Column(Integer, nullable=False)
    require_account_level_consent = Column(Integer, nullable=False)


class EnterpriseEnterprisecustomerbrandingconfiguration(Base):
    __tablename__ = 'enterprise_enterprisecustomerbrandingconfiguration'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    logo = Column(String(255))
    enterprise_customer_id = Column(String(32), nullable=False)


class EnterpriseEnterprisecustomerentitlement(Base):
    __tablename__ = 'enterprise_enterprisecustomerentitlement'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    entitlement_id = Column(Integer, nullable=False)
    enterprise_customer_id = Column(String(32), nullable=False)


class EnterpriseEnterprisecustomeridentityprovider(Base):
    __tablename__ = 'enterprise_enterprisecustomeridentityprovider'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    provider_id = Column(String(50), nullable=False)
    enterprise_customer_id = Column(String(32), nullable=False)


class EnterpriseEnterprisecustomeruser(Base):
    __tablename__ = 'enterprise_enterprisecustomeruser'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    user_id = Column(Integer, nullable=False)
    enterprise_customer_id = Column(String(32), nullable=False)


class EnterpriseHistoricalenrollmentnotificationemailtemplate(Base):
    __tablename__ = 'enterprise_historicalenrollmentnotificationemailtemplate'

    id = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    plaintext_template = Column(String, nullable=False)
    html_template = Column(String, nullable=False)
    subject_line = Column(String(100), nullable=False)
    history_id = Column(Integer, primary_key=True)
    history_date = Column(DateTime, nullable=False)
    history_type = Column(String(1), nullable=False)
    history_user_id = Column(Integer)
    site_id = Column(Integer)


class EnterpriseHistoricalenterprisecourseenrollment(Base):
    __tablename__ = 'enterprise_historicalenterprisecourseenrollment'

    id = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    consent_granted = Column(Integer)
    course_id = Column(String(255), nullable=False)
    history_id = Column(Integer, primary_key=True)
    history_date = Column(DateTime, nullable=False)
    history_type = Column(String(1), nullable=False)
    enterprise_customer_user_id = Column(Integer)
    history_user_id = Column(Integer)


class EnterpriseHistoricalenterprisecustomer(Base):
    __tablename__ = 'enterprise_historicalenterprisecustomer'

    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    uuid = Column(String(32), nullable=False)
    name = Column(String(255), nullable=False)
    active = Column(Integer, nullable=False)
    history_id = Column(Integer, primary_key=True)
    history_date = Column(DateTime, nullable=False)
    history_type = Column(String(1), nullable=False)
    history_user_id = Column(Integer)
    site_id = Column(Integer)
    catalog = Column(Integer)
    enable_data_sharing_consent = Column(Integer, nullable=False)
    enforce_data_sharing_consent = Column(String(25), nullable=False)
    enable_audit_enrollment = Column(Integer, nullable=False)
    require_account_level_consent = Column(Integer, nullable=False)


class EnterpriseHistoricalenterprisecustomerentitlement(Base):
    __tablename__ = 'enterprise_historicalenterprisecustomerentitlement'

    id = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    entitlement_id = Column(Integer, nullable=False)
    history_id = Column(Integer, primary_key=True)
    history_date = Column(DateTime, nullable=False)
    history_type = Column(String(1), nullable=False)
    enterprise_customer_id = Column(String(32))
    history_user_id = Column(Integer)


class EnterpriseHistoricaluserdatasharingconsentaudit(Base):
    __tablename__ = 'enterprise_historicaluserdatasharingconsentaudit'

    id = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    state = Column(String(8), nullable=False)
    history_id = Column(Integer, primary_key=True)
    history_date = Column(DateTime, nullable=False)
    history_type = Column(String(1), nullable=False)
    history_user_id = Column(Integer)
    user_id = Column(Integer)


class EnterprisePendingenrollment(Base):
    __tablename__ = 'enterprise_pendingenrollment'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_id = Column(String(255), nullable=False)
    course_mode = Column(String(25), nullable=False)
    user_id = Column(Integer, nullable=False)


class EnterprisePendingenterprisecustomeruser(Base):
    __tablename__ = 'enterprise_pendingenterprisecustomeruser'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    user_email = Column(String(254), nullable=False)
    enterprise_customer_id = Column(String(32), nullable=False)


class EnterpriseUserdatasharingconsentaudit(Base):
    __tablename__ = 'enterprise_userdatasharingconsentaudit'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    state = Column(String(8), nullable=False)
    user_id = Column(Integer, nullable=False)


class ExperimentsExperimentdata(Base):
    __tablename__ = 'experiments_experimentdata'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    experiment_id = Column(SmallInteger, nullable=False)
    key = Column(String(255), nullable=False)
    value = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)


class ExperimentsExperimentkeyvalue(Base):
    __tablename__ = 'experiments_experimentkeyvalue'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    experiment_id = Column(SmallInteger, nullable=False)
    key = Column(String(255), nullable=False)
    value = Column(String, nullable=False)


class ExternalAuthExternalauthmap(Base):
    __tablename__ = 'external_auth_externalauthmap'

    id = Column(Integer, primary_key=True)
    external_id = Column(String(255), nullable=False)
    external_domain = Column(String(255), nullable=False)
    external_credentials = Column(String, nullable=False)
    external_email = Column(String(255), nullable=False)
    external_name = Column(String(255), nullable=False)
    internal_password = Column(String(31), nullable=False)
    dtcreated = Column(DateTime, nullable=False)
    dtsignup = Column(DateTime)
    user_id = Column(Integer)


class GradesComputegradessetting(Base):
    __tablename__ = 'grades_computegradessetting'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    batch_size = Column(Integer, nullable=False)
    course_ids = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class GradesCoursepersistentgradesflag(Base):
    __tablename__ = 'grades_coursepersistentgradesflag'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    course_id = Column(String(255), nullable=False)
    changed_by_id = Column(Integer)


class GradesPersistentcoursegrade(Base):
    __tablename__ = 'grades_persistentcoursegrade'

    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    id = Column(BigInteger, primary_key=True)
    user_id = Column(Integer, nullable=False)
    course_id = Column(String(255), nullable=False)
    course_edited_timestamp = Column(DateTime)
    course_version = Column(String(255), nullable=False)
    grading_policy_hash = Column(String(255), nullable=False)
    percent_grade = Column(Float(asdecimal=True), nullable=False)
    letter_grade = Column(String(255), nullable=False)
    passed_timestamp = Column(DateTime)


class GradesPersistentgradesenabledflag(Base):
    __tablename__ = 'grades_persistentgradesenabledflag'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    enabled_for_all_courses = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class GradesPersistentsubsectiongrade(Base):
    __tablename__ = 'grades_persistentsubsectiongrade'

    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    id = Column(BigInteger, primary_key=True)
    user_id = Column(Integer, nullable=False)
    course_id = Column(String(255), nullable=False)
    usage_key = Column(String(255), nullable=False)
    subtree_edited_timestamp = Column(DateTime)
    course_version = Column(String(255), nullable=False)
    earned_all = Column(Float(asdecimal=True), nullable=False)
    possible_all = Column(Float(asdecimal=True), nullable=False)
    earned_graded = Column(Float(asdecimal=True), nullable=False)
    possible_graded = Column(Float(asdecimal=True), nullable=False)
    visible_blocks_hash = Column(String(100), nullable=False)
    first_attempted = Column(DateTime)


class GradesVisibleblocks(Base):
    __tablename__ = 'grades_visibleblocks'

    id = Column(Integer, primary_key=True)
    blocks_json = Column(String, nullable=False)
    hashed = Column(String(100), nullable=False)
    course_id = Column(String(255), nullable=False)


class InstructorTaskGradereportsetting(Base):
    __tablename__ = 'instructor_task_gradereportsetting'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    batch_size = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class InstructorTaskInstructortask(Base):
    __tablename__ = 'instructor_task_instructortask'

    id = Column(Integer, primary_key=True)
    task_type = Column(String(50), nullable=False)
    course_id = Column(String(255), nullable=False)
    task_key = Column(String(255), nullable=False)
    task_input = Column(String(255), nullable=False)
    task_id = Column(String(255), nullable=False)
    task_state = Column(String(50))
    task_output = Column(String(1024))
    created = Column(DateTime)
    updated = Column(DateTime, nullable=False)
    subtasks = Column(String, nullable=False)
    requester_id = Column(Integer, nullable=False)


class IntegratedChannelEnterpriseintegratedchannel(Base):
    __tablename__ = 'integrated_channel_enterpriseintegratedchannel'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    name = Column(String(255), nullable=False)
    data_type = Column(String(100), nullable=False)


class LmsXblockXblockasidesconfig(Base):
    __tablename__ = 'lms_xblock_xblockasidesconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    disabled_blocks = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class MicrositeConfigurationHistoricalmicrositeorganizationmapping(Base):
    __tablename__ = 'microsite_configuration_historicalmicrositeorganizationmapping'

    id = Column(Integer, nullable=False)
    organization = Column(String(63), nullable=False)
    history_id = Column(Integer, primary_key=True)
    history_date = Column(DateTime, nullable=False)
    history_type = Column(String(1), nullable=False)
    history_user_id = Column(Integer)
    microsite_id = Column(Integer)


class MicrositeConfigurationHistoricalmicrositetemplate(Base):
    __tablename__ = 'microsite_configuration_historicalmicrositetemplate'

    id = Column(Integer, nullable=False)
    template_uri = Column(String(255), nullable=False)
    template = Column(String, nullable=False)
    history_id = Column(Integer, primary_key=True)
    history_date = Column(DateTime, nullable=False)
    history_type = Column(String(1), nullable=False)
    history_user_id = Column(Integer)
    microsite_id = Column(Integer)


class MicrositeConfigurationMicrosite(Base):
    __tablename__ = 'microsite_configuration_microsite'

    id = Column(Integer, primary_key=True)
    key = Column(String(63), nullable=False)
    values = Column(String, nullable=False)
    site_id = Column(Integer, nullable=False)


class MicrositeConfigurationMicrositehistory(Base):
    __tablename__ = 'microsite_configuration_micrositehistory'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    key = Column(String(63), nullable=False)
    values = Column(String, nullable=False)
    site_id = Column(Integer, nullable=False)


class MicrositeConfigurationMicrositeorganizationmapping(Base):
    __tablename__ = 'microsite_configuration_micrositeorganizationmapping'

    id = Column(Integer, primary_key=True)
    organization = Column(String(63), nullable=False)
    microsite_id = Column(Integer, nullable=False)


class MicrositeConfigurationMicrositetemplate(Base):
    __tablename__ = 'microsite_configuration_micrositetemplate'

    id = Column(Integer, primary_key=True)
    template_uri = Column(String(255), nullable=False)
    template = Column(String, nullable=False)
    microsite_id = Column(Integer, nullable=False)


class MilestonesCoursecontentmilestone(Base):
    __tablename__ = 'milestones_coursecontentmilestone'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_id = Column(String(255), nullable=False)
    content_id = Column(String(255), nullable=False)
    active = Column(Integer, nullable=False)
    milestone_id = Column(Integer, nullable=False)
    milestone_relationship_type_id = Column(Integer, nullable=False)
    requirements = Column(String(255))


class MilestonesCoursemilestone(Base):
    __tablename__ = 'milestones_coursemilestone'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_id = Column(String(255), nullable=False)
    active = Column(Integer, nullable=False)
    milestone_id = Column(Integer, nullable=False)
    milestone_relationship_type_id = Column(Integer, nullable=False)


class MilestonesMilestone(Base):
    __tablename__ = 'milestones_milestone'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    namespace = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    display_name = Column(String(255), nullable=False)
    description = Column(String, nullable=False)
    active = Column(Integer, nullable=False)


class MilestonesMilestonerelationshiptype(Base):
    __tablename__ = 'milestones_milestonerelationshiptype'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    name = Column(String(25), nullable=False)
    description = Column(String, nullable=False)
    active = Column(Integer, nullable=False)


class MilestonesUsermilestone(Base):
    __tablename__ = 'milestones_usermilestone'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    user_id = Column(Integer, nullable=False)
    source = Column(String, nullable=False)
    collected = Column(DateTime)
    active = Column(Integer, nullable=False)
    milestone_id = Column(Integer, nullable=False)


class MobileApiAppversionconfig(Base):
    __tablename__ = 'mobile_api_appversionconfig'

    id = Column(Integer, primary_key=True)
    platform = Column(String(50), nullable=False)
    version = Column(String(50), nullable=False)
    major_version = Column(Integer, nullable=False)
    minor_version = Column(Integer, nullable=False)
    patch_version = Column(Integer, nullable=False)
    expire_at = Column(DateTime)
    enabled = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class MobileApiIgnoremobileavailableflagconfig(Base):
    __tablename__ = 'mobile_api_ignoremobileavailableflagconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class MobileApiMobileapiconfig(Base):
    __tablename__ = 'mobile_api_mobileapiconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    video_profiles = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class NotesNote(Base):
    __tablename__ = 'notes_note'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    uri = Column(String(255), nullable=False)
    text = Column(String, nullable=False)
    quote = Column(String, nullable=False)
    range_start = Column(String(2048), nullable=False)
    range_start_offset = Column(Integer, nullable=False)
    range_end = Column(String(2048), nullable=False)
    range_end_offset = Column(Integer, nullable=False)
    tags = Column(String, nullable=False)
    created = Column(DateTime)
    updated = Column(DateTime, nullable=False)
    user_id = Column(Integer, nullable=False)


class NotifyNotification(Base):
    __tablename__ = 'notify_notification'

    id = Column(Integer, primary_key=True)
    message = Column(String, nullable=False)
    url = Column(String(200))
    is_viewed = Column(Integer, nullable=False)
    is_emailed = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    subscription_id = Column(Integer)


class NotifyNotificationtype(Base):
    __tablename__ = 'notify_notificationtype'

    key = Column(String(128), primary_key=True)
    label = Column(String(128))
    content_type_id = Column(Integer)


class NotifySettings(Base):
    __tablename__ = 'notify_settings'

    id = Column(Integer, primary_key=True)
    interval = Column(SmallInteger, nullable=False)
    user_id = Column(Integer, nullable=False)


class NotifySubscription(Base):
    __tablename__ = 'notify_subscription'

    subscription_id = Column(Integer, primary_key=True)
    object_id = Column(String(64))
    send_emails = Column(Integer, nullable=False)
    notification_type_id = Column(String(128), nullable=False)
    settings_id = Column(Integer, nullable=False)


class Oauth2Accesstoken(Base):
    __tablename__ = 'oauth2_accesstoken'

    id = Column(Integer, primary_key=True)
    token = Column(String(255), nullable=False)
    expires = Column(DateTime, nullable=False)
    scope = Column(Integer, nullable=False)
    client_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class Oauth2Client(Base):
    __tablename__ = 'oauth2_client'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    url = Column(String(200), nullable=False)
    redirect_uri = Column(String(200), nullable=False)
    client_id = Column(String(255), nullable=False)
    client_secret = Column(String(255), nullable=False)
    client_type = Column(Integer, nullable=False)
    user_id = Column(Integer)
    logout_uri = Column(String(200))


class Oauth2Grant(Base):
    __tablename__ = 'oauth2_grant'

    id = Column(Integer, primary_key=True)
    code = Column(String(255), nullable=False)
    expires = Column(DateTime, nullable=False)
    redirect_uri = Column(String(255), nullable=False)
    scope = Column(Integer, nullable=False)
    client_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class Oauth2ProviderAccesstoken(Base):
    __tablename__ = 'oauth2_provider_accesstoken'

    id = Column(Integer, primary_key=True)
    token = Column(String(255), nullable=False)
    expires = Column(DateTime, nullable=False)
    scope = Column(String, nullable=False)
    application_id = Column(Integer, nullable=False)
    user_id = Column(Integer)


class Oauth2ProviderApplication(Base):
    __tablename__ = 'oauth2_provider_application'

    id = Column(Integer, primary_key=True)
    client_id = Column(String(100), nullable=False)
    redirect_uris = Column(String, nullable=False)
    client_type = Column(String(32), nullable=False)
    authorization_grant_type = Column(String(32), nullable=False)
    client_secret = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    user_id = Column(Integer, nullable=False)
    skip_authorization = Column(Integer, nullable=False)


class Oauth2ProviderGrant(Base):
    __tablename__ = 'oauth2_provider_grant'

    id = Column(Integer, primary_key=True)
    code = Column(String(255), nullable=False)
    expires = Column(DateTime, nullable=False)
    redirect_uri = Column(String(255), nullable=False)
    scope = Column(String, nullable=False)
    application_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class Oauth2ProviderRefreshtoken(Base):
    __tablename__ = 'oauth2_provider_refreshtoken'

    id = Column(Integer, primary_key=True)
    token = Column(String(255), nullable=False)
    access_token_id = Column(Integer, nullable=False)
    application_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class Oauth2ProviderTrustedclient(Base):
    __tablename__ = 'oauth2_provider_trustedclient'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, nullable=False)


class Oauth2Refreshtoken(Base):
    __tablename__ = 'oauth2_refreshtoken'

    id = Column(Integer, primary_key=True)
    token = Column(String(255), nullable=False)
    expired = Column(Integer, nullable=False)
    access_token_id = Column(Integer, nullable=False)
    client_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class OauthDispatchRestrictedapplication(Base):
    __tablename__ = 'oauth_dispatch_restrictedapplication'

    id = Column(Integer, primary_key=True)
    application_id = Column(Integer, nullable=False)


class OauthProviderConsumer(Base):
    __tablename__ = 'oauth_provider_consumer'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String, nullable=False)
    key = Column(String(256), nullable=False)
    secret = Column(String(16), nullable=False)
    status = Column(SmallInteger, nullable=False)
    xauth_allowed = Column(Integer, nullable=False)
    user_id = Column(Integer)


class OauthProviderNonce(Base):
    __tablename__ = 'oauth_provider_nonce'

    id = Column(Integer, primary_key=True)
    token_key = Column(String(32), nullable=False)
    consumer_key = Column(String(256), nullable=False)
    key = Column(String(255), nullable=False)
    timestamp = Column(Integer, nullable=False)


class OauthProviderScope(Base):
    __tablename__ = 'oauth_provider_scope'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    url = Column(String, nullable=False)
    is_readonly = Column(Integer, nullable=False)


class OauthProviderToken(Base):
    __tablename__ = 'oauth_provider_token'

    id = Column(Integer, primary_key=True)
    key = Column(String(32))
    secret = Column(String(16))
    token_type = Column(SmallInteger, nullable=False)
    timestamp = Column(Integer, nullable=False)
    is_approved = Column(Integer, nullable=False)
    verifier = Column(String(10), nullable=False)
    callback = Column(String(2083))
    callback_confirmed = Column(Integer, nullable=False)
    consumer_id = Column(Integer, nullable=False)
    scope_id = Column(Integer)
    user_id = Column(Integer)


class OrganizationsOrganization(Base):
    __tablename__ = 'organizations_organization'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    name = Column(String(255), nullable=False)
    short_name = Column(String(255), nullable=False)
    description = Column(String)
    logo = Column(String(255))
    active = Column(Integer, nullable=False)


class OrganizationsOrganizationcourse(Base):
    __tablename__ = 'organizations_organizationcourse'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_id = Column(String(255), nullable=False)
    active = Column(Integer, nullable=False)
    organization_id = Column(Integer, nullable=False)


class ProctoringProctoredexam(Base):
    __tablename__ = 'proctoring_proctoredexam'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_id = Column(String(255), nullable=False)
    content_id = Column(String(255), nullable=False)
    external_id = Column(String(255))
    exam_name = Column(String, nullable=False)
    time_limit_mins = Column(Integer, nullable=False)
    due_date = Column(DateTime)
    is_proctored = Column(Integer, nullable=False)
    is_practice_exam = Column(Integer, nullable=False)
    is_active = Column(Integer, nullable=False)
    hide_after_due = Column(Integer, nullable=False)


class ProctoringProctoredexamreviewpolicy(Base):
    __tablename__ = 'proctoring_proctoredexamreviewpolicy'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    review_policy = Column(String, nullable=False)
    proctored_exam_id = Column(Integer, nullable=False)
    set_by_user_id = Column(Integer, nullable=False)


class ProctoringProctoredexamreviewpolicyhistory(Base):
    __tablename__ = 'proctoring_proctoredexamreviewpolicyhistory'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    original_id = Column(Integer, nullable=False)
    review_policy = Column(String, nullable=False)
    proctored_exam_id = Column(Integer, nullable=False)
    set_by_user_id = Column(Integer, nullable=False)


class ProctoringProctoredexamsoftwaresecurereview(Base):
    __tablename__ = 'proctoring_proctoredexamsoftwaresecurereview'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    attempt_code = Column(String(255), nullable=False)
    review_status = Column(String(255), nullable=False)
    raw_data = Column(String, nullable=False)
    video_url = Column(String, nullable=False)
    exam_id = Column(Integer)
    reviewed_by_id = Column(Integer)
    student_id = Column(Integer)


class ProctoringProctoredexamsoftwaresecurereviewhistory(Base):
    __tablename__ = 'proctoring_proctoredexamsoftwaresecurereviewhistory'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    attempt_code = Column(String(255), nullable=False)
    review_status = Column(String(255), nullable=False)
    raw_data = Column(String, nullable=False)
    video_url = Column(String, nullable=False)
    exam_id = Column(Integer)
    reviewed_by_id = Column(Integer)
    student_id = Column(Integer)


class ProctoringProctoredexamstudentallowance(Base):
    __tablename__ = 'proctoring_proctoredexamstudentallowance'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    key = Column(String(255), nullable=False)
    value = Column(String(255), nullable=False)
    proctored_exam_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class ProctoringProctoredexamstudentallowancehistory(Base):
    __tablename__ = 'proctoring_proctoredexamstudentallowancehistory'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    allowance_id = Column(Integer, nullable=False)
    key = Column(String(255), nullable=False)
    value = Column(String(255), nullable=False)
    proctored_exam_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class ProctoringProctoredexamstudentattempt(Base):
    __tablename__ = 'proctoring_proctoredexamstudentattempt'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    last_poll_timestamp = Column(DateTime)
    last_poll_ipaddr = Column(String(32))
    attempt_code = Column(String(255))
    external_id = Column(String(255))
    allowed_time_limit_mins = Column(Integer, nullable=False)
    status = Column(String(64), nullable=False)
    taking_as_proctored = Column(Integer, nullable=False)
    is_sample_attempt = Column(Integer, nullable=False)
    student_name = Column(String(255), nullable=False)
    review_policy_id = Column(Integer)
    proctored_exam_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    is_status_acknowledged = Column(Integer, nullable=False)


class ProctoringProctoredexamstudentattemptcomment(Base):
    __tablename__ = 'proctoring_proctoredexamstudentattemptcomment'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    start_time = Column(Integer, nullable=False)
    stop_time = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)
    comment = Column(String, nullable=False)
    status = Column(String(255), nullable=False)
    review_id = Column(Integer, nullable=False)


class ProctoringProctoredexamstudentattempthistory(Base):
    __tablename__ = 'proctoring_proctoredexamstudentattempthistory'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    attempt_id = Column(Integer)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    attempt_code = Column(String(255))
    external_id = Column(String(255))
    allowed_time_limit_mins = Column(Integer, nullable=False)
    status = Column(String(64), nullable=False)
    taking_as_proctored = Column(Integer, nullable=False)
    is_sample_attempt = Column(Integer, nullable=False)
    student_name = Column(String(255), nullable=False)
    review_policy_id = Column(Integer)
    last_poll_timestamp = Column(DateTime)
    last_poll_ipaddr = Column(String(32))
    proctored_exam_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class ProgramsProgramsapiconfig(Base):
    __tablename__ = 'programs_programsapiconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)
    marketing_path = Column(String(255), nullable=False)


class RssProxyWhitelistedrssurl(Base):
    __tablename__ = 'rss_proxy_whitelistedrssurl'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    url = Column(String(255), nullable=False)


class SapSuccessFactorsCatalogtransmissionaudit(Base):
    __tablename__ = 'sap_success_factors_catalogtransmissionaudit'

    id = Column(Integer, primary_key=True)
    enterprise_customer_uuid = Column(String(32), nullable=False)
    total_courses = Column(Integer, nullable=False)
    status = Column(String(100), nullable=False)
    error_message = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    audit_summary = Column(String, nullable=False)


class SapSuccessFactorsHistoricalsapsuccessfactorsenterprisecus80ad(Base):
    __tablename__ = 'sap_success_factors_historicalsapsuccessfactorsenterprisecus80ad'

    id = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    active = Column(Integer, nullable=False)
    sapsf_base_url = Column(String(255), nullable=False)
    key = Column(String(255), nullable=False)
    secret = Column(String(255), nullable=False)
    history_id = Column(Integer, primary_key=True)
    history_date = Column(DateTime, nullable=False)
    history_type = Column(String(1), nullable=False)
    enterprise_customer_id = Column(String(32))
    history_user_id = Column(Integer)
    sapsf_company_id = Column(String(255), nullable=False)
    sapsf_user_id = Column(String(255), nullable=False)
    user_type = Column(String(20), nullable=False)


class SapSuccessFactorsLearnerdatatransmissionaudit(Base):
    __tablename__ = 'sap_success_factors_learnerdatatransmissionaudit'

    id = Column(Integer, primary_key=True)
    enterprise_course_enrollment_id = Column(Integer, nullable=False)
    sapsf_user_id = Column(String(255), nullable=False)
    course_id = Column(String(255), nullable=False)
    course_completed = Column(Integer, nullable=False)
    completed_timestamp = Column(BigInteger, nullable=False)
    instructor_name = Column(String(255), nullable=False)
    grade = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False)
    error_message = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)


class SapSuccessFactorsSapsuccessfactorsenterprisecustomerconfidb8a(Base):
    __tablename__ = 'sap_success_factors_sapsuccessfactorsenterprisecustomerconfidb8a'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    active = Column(Integer, nullable=False)
    sapsf_base_url = Column(String(255), nullable=False)
    key = Column(String(255), nullable=False)
    secret = Column(String(255), nullable=False)
    enterprise_customer_id = Column(String(32), nullable=False)
    sapsf_company_id = Column(String(255), nullable=False)
    sapsf_user_id = Column(String(255), nullable=False)
    user_type = Column(String(20), nullable=False)


class SapSuccessFactorsSapsuccessfactorsglobalconfiguration(Base):
    __tablename__ = 'sap_success_factors_sapsuccessfactorsglobalconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    completion_status_api_path = Column(String(255), nullable=False)
    course_api_path = Column(String(255), nullable=False)
    oauth_api_path = Column(String(255), nullable=False)
    provider_id = Column(String(100), nullable=False)
    changed_by_id = Column(Integer)


class SelfPacedSelfpacedconfiguration(Base):
    __tablename__ = 'self_paced_selfpacedconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    enable_course_home_improvements = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class ShoppingcartCertificateitem(Base):
    __tablename__ = 'shoppingcart_certificateitem'

    orderitem_ptr_id = Column(Integer, primary_key=True)
    course_id = Column(String(128), nullable=False)
    mode = Column(String(50), nullable=False)
    course_enrollment_id = Column(Integer, nullable=False)


class ShoppingcartCoupon(Base):
    __tablename__ = 'shoppingcart_coupon'

    id = Column(Integer, primary_key=True)
    code = Column(String(32), nullable=False)
    description = Column(String(255))
    course_id = Column(String(255), nullable=False)
    percentage_discount = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    is_active = Column(Integer, nullable=False)
    expiration_date = Column(DateTime)
    created_by_id = Column(Integer, nullable=False)


class ShoppingcartCouponredemption(Base):
    __tablename__ = 'shoppingcart_couponredemption'

    id = Column(Integer, primary_key=True)
    coupon_id = Column(Integer, nullable=False)
    order_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class ShoppingcartCourseregcodeitem(Base):
    __tablename__ = 'shoppingcart_courseregcodeitem'

    orderitem_ptr_id = Column(Integer, primary_key=True)
    course_id = Column(String(128), nullable=False)
    mode = Column(String(50), nullable=False)


class ShoppingcartCourseregcodeitemannotation(Base):
    __tablename__ = 'shoppingcart_courseregcodeitemannotation'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(128), nullable=False)
    annotation = Column(String)


class ShoppingcartCourseregistrationcode(Base):
    __tablename__ = 'shoppingcart_courseregistrationcode'

    id = Column(Integer, primary_key=True)
    code = Column(String(32), nullable=False)
    course_id = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    mode_slug = Column(String(100))
    is_valid = Column(Integer, nullable=False)
    created_by_id = Column(Integer, nullable=False)
    invoice_id = Column(Integer)
    order_id = Column(Integer)
    invoice_item_id = Column(Integer)


class ShoppingcartCourseregistrationcodeinvoiceitem(Base):
    __tablename__ = 'shoppingcart_courseregistrationcodeinvoiceitem'

    invoiceitem_ptr_id = Column(Integer, primary_key=True)
    course_id = Column(String(128), nullable=False)


class ShoppingcartDonation(Base):
    __tablename__ = 'shoppingcart_donation'

    orderitem_ptr_id = Column(Integer, primary_key=True)
    donation_type = Column(String(32), nullable=False)
    course_id = Column(String(255), nullable=False)


class ShoppingcartDonationconfiguration(Base):
    __tablename__ = 'shoppingcart_donationconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class ShoppingcartInvoice(Base):
    __tablename__ = 'shoppingcart_invoice'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    company_name = Column(String(255), nullable=False)
    company_contact_name = Column(String(255), nullable=False)
    company_contact_email = Column(String(255), nullable=False)
    recipient_name = Column(String(255), nullable=False)
    recipient_email = Column(String(255), nullable=False)
    address_line_1 = Column(String(255), nullable=False)
    address_line_2 = Column(String(255))
    address_line_3 = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    zip = Column(String(15))
    country = Column(String(64))
    total_amount = Column(Float(asdecimal=True), nullable=False)
    course_id = Column(String(255), nullable=False)
    internal_reference = Column(String(255))
    customer_reference_number = Column(String(63))
    is_valid = Column(Integer, nullable=False)


class ShoppingcartInvoicehistory(Base):
    __tablename__ = 'shoppingcart_invoicehistory'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    snapshot = Column(String, nullable=False)
    invoice_id = Column(Integer, nullable=False)


class ShoppingcartInvoiceitem(Base):
    __tablename__ = 'shoppingcart_invoiceitem'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    qty = Column(Integer, nullable=False)
    unit_price = Column(Numeric(30, 2), nullable=False)
    currency = Column(String(8), nullable=False)
    invoice_id = Column(Integer, nullable=False)


class ShoppingcartInvoicetransaction(Base):
    __tablename__ = 'shoppingcart_invoicetransaction'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    amount = Column(Numeric(30, 2), nullable=False)
    currency = Column(String(8), nullable=False)
    comments = Column(String)
    status = Column(String(32), nullable=False)
    created_by_id = Column(Integer, nullable=False)
    invoice_id = Column(Integer, nullable=False)
    last_modified_by_id = Column(Integer, nullable=False)


class ShoppingcartOrder(Base):
    __tablename__ = 'shoppingcart_order'

    id = Column(Integer, primary_key=True)
    currency = Column(String(8), nullable=False)
    status = Column(String(32), nullable=False)
    purchase_time = Column(DateTime)
    refunded_time = Column(DateTime)
    bill_to_first = Column(String(64), nullable=False)
    bill_to_last = Column(String(64), nullable=False)
    bill_to_street1 = Column(String(128), nullable=False)
    bill_to_street2 = Column(String(128), nullable=False)
    bill_to_city = Column(String(64), nullable=False)
    bill_to_state = Column(String(8), nullable=False)
    bill_to_postalcode = Column(String(16), nullable=False)
    bill_to_country = Column(String(64), nullable=False)
    bill_to_ccnum = Column(String(8), nullable=False)
    bill_to_cardtype = Column(String(32), nullable=False)
    processor_reply_dump = Column(String, nullable=False)
    company_name = Column(String(255))
    company_contact_name = Column(String(255))
    company_contact_email = Column(String(255))
    recipient_name = Column(String(255))
    recipient_email = Column(String(255))
    customer_reference_number = Column(String(63))
    order_type = Column(String(32), nullable=False)
    user_id = Column(Integer, nullable=False)


class ShoppingcartOrderitem(Base):
    __tablename__ = 'shoppingcart_orderitem'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    status = Column(String(32), nullable=False)
    qty = Column(Integer, nullable=False)
    unit_cost = Column(Numeric(30, 2), nullable=False)
    list_price = Column(Numeric(30, 2))
    line_desc = Column(String(1024), nullable=False)
    currency = Column(String(8), nullable=False)
    fulfilled_time = Column(DateTime)
    refund_requested_time = Column(DateTime)
    service_fee = Column(Numeric(30, 2), nullable=False)
    report_comments = Column(String, nullable=False)
    order_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class ShoppingcartPaidcourseregistration(Base):
    __tablename__ = 'shoppingcart_paidcourseregistration'

    orderitem_ptr_id = Column(Integer, primary_key=True)
    course_id = Column(String(128), nullable=False)
    mode = Column(String(50), nullable=False)
    course_enrollment_id = Column(Integer)


class ShoppingcartPaidcourseregistrationannotation(Base):
    __tablename__ = 'shoppingcart_paidcourseregistrationannotation'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(128), nullable=False)
    annotation = Column(String)


class ShoppingcartRegistrationcoderedemption(Base):
    __tablename__ = 'shoppingcart_registrationcoderedemption'

    id = Column(Integer, primary_key=True)
    redeemed_at = Column(DateTime)
    course_enrollment_id = Column(Integer)
    order_id = Column(Integer)
    redeemed_by_id = Column(Integer, nullable=False)
    registration_code_id = Column(Integer, nullable=False)


class SiteConfigurationSiteconfiguration(Base):
    __tablename__ = 'site_configuration_siteconfiguration'

    id = Column(Integer, primary_key=True)
    values = Column(String, nullable=False)
    site_id = Column(Integer, nullable=False)
    enabled = Column(Integer, nullable=False)


class SiteConfigurationSiteconfigurationhistory(Base):
    __tablename__ = 'site_configuration_siteconfigurationhistory'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    values = Column(String, nullable=False)
    site_id = Column(Integer, nullable=False)
    enabled = Column(Integer, nullable=False)


class SocialAuthAssociation(Base):
    __tablename__ = 'social_auth_association'

    id = Column(Integer, primary_key=True)
    server_url = Column(String(255), nullable=False)
    handle = Column(String(255), nullable=False)
    secret = Column(String(255), nullable=False)
    issued = Column(Integer, nullable=False)
    lifetime = Column(Integer, nullable=False)
    assoc_type = Column(String(64), nullable=False)


class SocialAuthCode(Base):
    __tablename__ = 'social_auth_code'

    id = Column(Integer, primary_key=True)
    email = Column(String(254), nullable=False)
    code = Column(String(32), nullable=False)
    verified = Column(Integer, nullable=False)


class SocialAuthNonce(Base):
    __tablename__ = 'social_auth_nonce'

    id = Column(Integer, primary_key=True)
    server_url = Column(String(255), nullable=False)
    timestamp = Column(Integer, nullable=False)
    salt = Column(String(65), nullable=False)


class SocialAuthPartial(Base):
    __tablename__ = 'social_auth_partial'

    id = Column(Integer, primary_key=True)
    token = Column(String(32), nullable=False)
    next_step = Column(SmallInteger, nullable=False)
    backend = Column(String(32), nullable=False)
    data = Column(String, nullable=False)


class SocialAuthUsersocialauth(Base):
    __tablename__ = 'social_auth_usersocialauth'

    id = Column(Integer, primary_key=True)
    provider = Column(String(32), nullable=False)
    uid = Column(String(255), nullable=False)
    extra_data = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)


class SplashSplashconfig(Base):
    __tablename__ = 'splash_splashconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    cookie_name = Column(String, nullable=False)
    cookie_allowed_values = Column(String, nullable=False)
    unaffected_usernames = Column(String, nullable=False)
    unaffected_url_paths = Column(String, nullable=False)
    redirect_url = Column(String(200), nullable=False)
    changed_by_id = Column(Integer)


class StaticReplaceAssetbaseurlconfig(Base):
    __tablename__ = 'static_replace_assetbaseurlconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    base_url = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class StaticReplaceAssetexcludedextensionsconfig(Base):
    __tablename__ = 'static_replace_assetexcludedextensionsconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    excluded_extensions = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class StatusCoursemessage(Base):
    __tablename__ = 'status_coursemessage'

    id = Column(Integer, primary_key=True)
    course_key = Column(String(255), nullable=False)
    message = Column(String)
    global_message_id = Column(Integer, nullable=False)


class StatusGlobalstatusmessage(Base):
    __tablename__ = 'status_globalstatusmessage'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    message = Column(String)
    changed_by_id = Column(Integer)


class StudentAnonymoususerid(Base):
    __tablename__ = 'student_anonymoususerid'

    id = Column(Integer, primary_key=True)
    anonymous_user_id = Column(String(32), nullable=False)
    course_id = Column(String(255), nullable=False)
    user_id = Column(Integer, nullable=False)


class StudentCourseaccessrole(Base):
    __tablename__ = 'student_courseaccessrole'

    id = Column(Integer, primary_key=True)
    org = Column(String(64), nullable=False)
    course_id = Column(String(255), nullable=False)
    role = Column(String(64), nullable=False)
    user_id = Column(Integer, nullable=False)


class StudentCourseenrollment(Base):
    __tablename__ = 'student_courseenrollment'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    created = Column(DateTime)
    is_active = Column(Integer, nullable=False)
    mode = Column(String(100), nullable=False)
    user_id = Column(Integer, nullable=False)


class StudentCourseenrollmentallowed(Base):
    __tablename__ = 'student_courseenrollmentallowed'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    course_id = Column(String(255), nullable=False)
    auto_enroll = Column(Integer, nullable=False)
    created = Column(DateTime)


class StudentCourseenrollmentattribute(Base):
    __tablename__ = 'student_courseenrollmentattribute'

    id = Column(Integer, primary_key=True)
    namespace = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    value = Column(String(255), nullable=False)
    enrollment_id = Column(Integer, nullable=False)


class StudentDashboardconfiguration(Base):
    __tablename__ = 'student_dashboardconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    recent_enrollment_time_delta = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class StudentEnrollmentrefundconfiguration(Base):
    __tablename__ = 'student_enrollmentrefundconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    refund_window_microseconds = Column(BigInteger, nullable=False)
    changed_by_id = Column(Integer)


class StudentEntranceexamconfiguration(Base):
    __tablename__ = 'student_entranceexamconfiguration'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    created = Column(DateTime)
    updated = Column(DateTime, nullable=False)
    skip_entrance_exam = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class StudentHistoricalcourseenrollment(Base):
    __tablename__ = 'student_historicalcourseenrollment'

    id = Column(Integer, nullable=False)
    course_id = Column(String(255), nullable=False)
    created = Column(DateTime)
    is_active = Column(Integer, nullable=False)
    mode = Column(String(100), nullable=False)
    history_id = Column(Integer, primary_key=True)
    history_date = Column(DateTime, nullable=False)
    history_type = Column(String(1), nullable=False)
    history_user_id = Column(Integer)
    user_id = Column(Integer)


class StudentLanguageproficiency(Base):
    __tablename__ = 'student_languageproficiency'

    id = Column(Integer, primary_key=True)
    code = Column(String(16), nullable=False)
    user_profile_id = Column(Integer, nullable=False)


class StudentLinkedinaddtoprofileconfiguration(Base):
    __tablename__ = 'student_linkedinaddtoprofileconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    company_identifier = Column(String, nullable=False)
    dashboard_tracking_code = Column(String, nullable=False)
    trk_partner_name = Column(String(10), nullable=False)
    changed_by_id = Column(Integer)


class StudentLoginfailures(Base):
    __tablename__ = 'student_loginfailures'

    id = Column(Integer, primary_key=True)
    failure_count = Column(Integer, nullable=False)
    lockout_until = Column(DateTime)
    user_id = Column(Integer, nullable=False)


class StudentLogoutviewconfiguration(Base):
    __tablename__ = 'student_logoutviewconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class StudentManualenrollmentaudit(Base):
    __tablename__ = 'student_manualenrollmentaudit'

    id = Column(Integer, primary_key=True)
    enrolled_email = Column(String(255), nullable=False)
    time_stamp = Column(DateTime)
    state_transition = Column(String(255), nullable=False)
    reason = Column(String)
    enrolled_by_id = Column(Integer)
    enrollment_id = Column(Integer)


class StudentPasswordhistory(Base):
    __tablename__ = 'student_passwordhistory'

    id = Column(Integer, primary_key=True)
    password = Column(String(128), nullable=False)
    time_set = Column(DateTime, nullable=False)
    user_id = Column(Integer, nullable=False)


class StudentPendingemailchange(Base):
    __tablename__ = 'student_pendingemailchange'

    id = Column(Integer, primary_key=True)
    new_email = Column(String(255), nullable=False)
    activation_key = Column(String(32), nullable=False)
    user_id = Column(Integer, nullable=False)


class StudentPendingnamechange(Base):
    __tablename__ = 'student_pendingnamechange'

    id = Column(Integer, primary_key=True)
    new_name = Column(String(255), nullable=False)
    rationale = Column(String(1024), nullable=False)
    user_id = Column(Integer, nullable=False)


class StudentRegistrationcookieconfiguration(Base):
    __tablename__ = 'student_registrationcookieconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    utm_cookie_name = Column(String(255), nullable=False)
    affiliate_cookie_name = Column(String(255), nullable=False)
    changed_by_id = Column(Integer)


class StudentUserattribute(Base):
    __tablename__ = 'student_userattribute'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    name = Column(String(255), nullable=False)
    value = Column(String(255), nullable=False)
    user_id = Column(Integer, nullable=False)


class StudentUsersignupsource(Base):
    __tablename__ = 'student_usersignupsource'

    id = Column(Integer, primary_key=True)
    site = Column(String(255), nullable=False)
    user_id = Column(Integer, nullable=False)


class StudentUserstanding(Base):
    __tablename__ = 'student_userstanding'

    id = Column(Integer, primary_key=True)
    account_status = Column(String(31), nullable=False)
    standing_last_changed_at = Column(DateTime, nullable=False)
    changed_by_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class StudentUsertestgroup(Base):
    __tablename__ = 'student_usertestgroup'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    description = Column(String, nullable=False)


class StudentUsertestgroupUsers(Base):
    __tablename__ = 'student_usertestgroup_users'

    id = Column(Integer, primary_key=True)
    usertestgroup_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class SubmissionsScore(Base):
    __tablename__ = 'submissions_score'

    id = Column(Integer, primary_key=True)
    points_earned = Column(Integer, nullable=False)
    points_possible = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    reset = Column(Integer, nullable=False)
    student_item_id = Column(Integer, nullable=False)
    submission_id = Column(Integer)


class SubmissionsScoreannotation(Base):
    __tablename__ = 'submissions_scoreannotation'

    id = Column(Integer, primary_key=True)
    annotation_type = Column(String(255), nullable=False)
    creator = Column(String(255), nullable=False)
    reason = Column(String, nullable=False)
    score_id = Column(Integer, nullable=False)


class SubmissionsScoresummary(Base):
    __tablename__ = 'submissions_scoresummary'

    id = Column(Integer, primary_key=True)
    highest_id = Column(Integer, nullable=False)
    latest_id = Column(Integer, nullable=False)
    student_item_id = Column(Integer, nullable=False)


class SubmissionsStudentitem(Base):
    __tablename__ = 'submissions_studentitem'

    id = Column(Integer, primary_key=True)
    student_id = Column(String(255), nullable=False)
    course_id = Column(String(255), nullable=False)
    item_id = Column(String(255), nullable=False)
    item_type = Column(String(100), nullable=False)


class SubmissionsSubmission(Base):
    __tablename__ = 'submissions_submission'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), nullable=False)
    attempt_number = Column(Integer, nullable=False)
    submitted_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)
    raw_answer = Column(String, nullable=False)
    student_item_id = Column(Integer, nullable=False)
    status = Column(String(1), nullable=False)


class SurveySurveyanswer(Base):
    __tablename__ = 'survey_surveyanswer'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    field_name = Column(String(255), nullable=False)
    field_value = Column(String(1024), nullable=False)
    course_key = Column(String(255))
    form_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class SurveySurveyform(Base):
    __tablename__ = 'survey_surveyform'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    name = Column(String(255), nullable=False)
    form = Column(String, nullable=False)


class TaggingTagavailablevalues(Base):
    __tablename__ = 'tagging_tagavailablevalues'

    id = Column(Integer, primary_key=True)
    value = Column(String(255), nullable=False)
    category_id = Column(Integer, nullable=False)


class TaggingTagcategories(Base):
    __tablename__ = 'tagging_tagcategories'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)


class TeamsCourseteam(Base):
    __tablename__ = 'teams_courseteam'

    id = Column(Integer, primary_key=True)
    team_id = Column(String(255), nullable=False)
    discussion_topic_id = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    course_id = Column(String(255), nullable=False)
    topic_id = Column(String(255), nullable=False)
    date_created = Column(DateTime, nullable=False)
    description = Column(String(300), nullable=False)
    country = Column(String(2), nullable=False)
    language = Column(String(16), nullable=False)
    last_activity_at = Column(DateTime, nullable=False)
    team_size = Column(Integer, nullable=False)


class TeamsCourseteammembership(Base):
    __tablename__ = 'teams_courseteammembership'

    id = Column(Integer, primary_key=True)
    date_joined = Column(DateTime, nullable=False)
    last_activity_at = Column(DateTime, nullable=False)
    team_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class ThemingSitetheme(Base):
    __tablename__ = 'theming_sitetheme'

    id = Column(Integer, primary_key=True)
    theme_dir_name = Column(String(255), nullable=False)
    site_id = Column(Integer, nullable=False)


class ThirdPartyAuthLtiproviderconfig(Base):
    __tablename__ = 'third_party_auth_ltiproviderconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    icon_class = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    secondary = Column(Integer, nullable=False)
    skip_registration_form = Column(Integer, nullable=False)
    skip_email_verification = Column(Integer, nullable=False)
    lti_consumer_key = Column(String(255), nullable=False)
    lti_hostname = Column(String(255), nullable=False)
    lti_consumer_secret = Column(String(255), nullable=False)
    lti_max_timestamp_age = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)
    icon_image = Column(String(100), nullable=False)
    visible = Column(Integer, nullable=False)
    site_id = Column(Integer, nullable=False)
    drop_existing_session = Column(Integer, nullable=False)
    max_session_length = Column(Integer)
    skip_hinted_login_dialog = Column(Integer, nullable=False)
    send_to_registration_first = Column(Integer, nullable=False)


class ThirdPartyAuthOauth2providerconfig(Base):
    __tablename__ = 'third_party_auth_oauth2providerconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    icon_class = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    secondary = Column(Integer, nullable=False)
    skip_registration_form = Column(Integer, nullable=False)
    skip_email_verification = Column(Integer, nullable=False)
    backend_name = Column(String(50), nullable=False)
    key = Column(String, nullable=False)
    secret = Column(String, nullable=False)
    other_settings = Column(String, nullable=False)
    changed_by_id = Column(Integer)
    icon_image = Column(String(100), nullable=False)
    visible = Column(Integer, nullable=False)
    provider_slug = Column(String(30), nullable=False)
    site_id = Column(Integer, nullable=False)
    drop_existing_session = Column(Integer, nullable=False)
    max_session_length = Column(Integer)
    skip_hinted_login_dialog = Column(Integer, nullable=False)
    send_to_registration_first = Column(Integer, nullable=False)


class ThirdPartyAuthProviderapipermissions(Base):
    __tablename__ = 'third_party_auth_providerapipermissions'

    id = Column(Integer, primary_key=True)
    provider_id = Column(String(255), nullable=False)
    client_id = Column(Integer, nullable=False)


class ThirdPartyAuthSamlconfiguration(Base):
    __tablename__ = 'third_party_auth_samlconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    private_key = Column(String, nullable=False)
    public_key = Column(String, nullable=False)
    entity_id = Column(String(255), nullable=False)
    org_info_str = Column(String, nullable=False)
    other_config_str = Column(String, nullable=False)
    changed_by_id = Column(Integer)
    site_id = Column(Integer, nullable=False)


class ThirdPartyAuthSamlproviderconfig(Base):
    __tablename__ = 'third_party_auth_samlproviderconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    icon_class = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    secondary = Column(Integer, nullable=False)
    skip_registration_form = Column(Integer, nullable=False)
    skip_email_verification = Column(Integer, nullable=False)
    backend_name = Column(String(50), nullable=False)
    idp_slug = Column(String(30), nullable=False)
    entity_id = Column(String(255), nullable=False)
    metadata_source = Column(String(255), nullable=False)
    attr_user_permanent_id = Column(String(128), nullable=False)
    attr_full_name = Column(String(128), nullable=False)
    attr_first_name = Column(String(128), nullable=False)
    attr_last_name = Column(String(128), nullable=False)
    attr_username = Column(String(128), nullable=False)
    attr_email = Column(String(128), nullable=False)
    other_settings = Column(String, nullable=False)
    changed_by_id = Column(Integer)
    icon_image = Column(String(100), nullable=False)
    debug_mode = Column(Integer, nullable=False)
    visible = Column(Integer, nullable=False)
    site_id = Column(Integer, nullable=False)
    automatic_refresh_enabled = Column(Integer, nullable=False)
    identity_provider_type = Column(String(128), nullable=False)
    drop_existing_session = Column(Integer, nullable=False)
    max_session_length = Column(Integer)
    skip_hinted_login_dialog = Column(Integer, nullable=False)
    send_to_registration_first = Column(Integer, nullable=False)


class ThirdPartyAuthSamlproviderdata(Base):
    __tablename__ = 'third_party_auth_samlproviderdata'

    id = Column(Integer, primary_key=True)
    fetched_at = Column(DateTime, nullable=False)
    expires_at = Column(DateTime)
    entity_id = Column(String(255), nullable=False)
    sso_url = Column(String(200), nullable=False)
    public_key = Column(String, nullable=False)


class ThumbnailKvstore(Base):
    __tablename__ = 'thumbnail_kvstore'

    key = Column(String(200), primary_key=True)
    value = Column(String, nullable=False)


class TrackTrackinglog(Base):
    __tablename__ = 'track_trackinglog'

    id = Column(Integer, primary_key=True)
    dtcreated = Column(DateTime, nullable=False)
    username = Column(String(32), nullable=False)
    ip = Column(String(32), nullable=False)
    event_source = Column(String(32), nullable=False)
    event_type = Column(String(512), nullable=False)
    event = Column(String, nullable=False)
    agent = Column(String(256), nullable=False)
    page = Column(String(512))
    time = Column(DateTime, nullable=False)
    host = Column(String(64), nullable=False)


class UserApiUsercoursetag(Base):
    __tablename__ = 'user_api_usercoursetag'

    id = Column(Integer, primary_key=True)
    key = Column(String(255), nullable=False)
    course_id = Column(String(255), nullable=False)
    value = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)


class UserApiUserorgtag(Base):
    __tablename__ = 'user_api_userorgtag'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    key = Column(String(255), nullable=False)
    org = Column(String(255), nullable=False)
    value = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)


class UserApiUserpreference(Base):
    __tablename__ = 'user_api_userpreference'

    id = Column(Integer, primary_key=True)
    key = Column(String(255), nullable=False)
    value = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)


class UserTasksUsertaskartifact(Base):
    __tablename__ = 'user_tasks_usertaskartifact'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    uuid = Column(String(32), nullable=False)
    name = Column(String(255), nullable=False)
    file = Column(String(100))
    url = Column(String(200), nullable=False)
    text = Column(String, nullable=False)
    status_id = Column(Integer, nullable=False)


class UserTasksUsertaskstatus(Base):
    __tablename__ = 'user_tasks_usertaskstatus'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    uuid = Column(String(32), nullable=False)
    task_id = Column(String(128), nullable=False)
    is_container = Column(Integer, nullable=False)
    task_class = Column(String(128), nullable=False)
    name = Column(String(255), nullable=False)
    state = Column(String(128), nullable=False)
    completed_steps = Column(SmallInteger, nullable=False)
    total_steps = Column(SmallInteger, nullable=False)
    attempts = Column(SmallInteger, nullable=False)
    parent_id = Column(Integer)
    user_id = Column(Integer, nullable=False)


class UtilRatelimitconfiguration(Base):
    __tablename__ = 'util_ratelimitconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class VerifiedTrackContentVerifiedtrackcohortedcourse(Base):
    __tablename__ = 'verified_track_content_verifiedtrackcohortedcourse'

    id = Column(Integer, primary_key=True)
    course_key = Column(String(255), nullable=False)
    enabled = Column(Integer, nullable=False)
    verified_cohort_name = Column(String(100), nullable=False)


class VerifyStudentHistoricalverificationdeadline(Base):
    __tablename__ = 'verify_student_historicalverificationdeadline'

    id = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_key = Column(String(255), nullable=False)
    deadline = Column(DateTime, nullable=False)
    history_id = Column(Integer, primary_key=True)
    history_date = Column(DateTime, nullable=False)
    history_type = Column(String(1), nullable=False)
    history_user_id = Column(Integer)
    deadline_is_explicit = Column(Integer, nullable=False)


class VerifyStudentIcrvstatusemailsconfiguration(Base):
    __tablename__ = 'verify_student_icrvstatusemailsconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class VerifyStudentIncoursereverificationconfiguration(Base):
    __tablename__ = 'verify_student_incoursereverificationconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class VerifyStudentSkippedreverification(Base):
    __tablename__ = 'verify_student_skippedreverification'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    checkpoint_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class VerifyStudentSoftwaresecurephotoverification(Base):
    __tablename__ = 'verify_student_softwaresecurephotoverification'

    id = Column(Integer, primary_key=True)
    status = Column(String(100), nullable=False)
    status_changed = Column(DateTime, nullable=False)
    name = Column(String(255), nullable=False)
    face_image_url = Column(String(255), nullable=False)
    photo_id_image_url = Column(String(255), nullable=False)
    receipt_id = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    display = Column(Integer, nullable=False)
    submitted_at = Column(DateTime)
    reviewing_service = Column(String(255), nullable=False)
    error_msg = Column(String, nullable=False)
    error_code = Column(String(50), nullable=False)
    photo_id_key = Column(String, nullable=False)
    copy_id_photo_from_id = Column(Integer)
    reviewing_user_id = Column(Integer)
    user_id = Column(Integer, nullable=False)


class VerifyStudentVerificationcheckpoint(Base):
    __tablename__ = 'verify_student_verificationcheckpoint'

    id = Column(Integer, primary_key=True)
    course_id = Column(String(255), nullable=False)
    checkpoint_location = Column(String(255), nullable=False)


class VerifyStudentVerificationcheckpointPhotoVerification(Base):
    __tablename__ = 'verify_student_verificationcheckpoint_photo_verification'

    id = Column(Integer, primary_key=True)
    verificationcheckpoint_id = Column(Integer, nullable=False)
    softwaresecurephotoverification_id = Column(Integer, nullable=False)


class VerifyStudentVerificationdeadline(Base):
    __tablename__ = 'verify_student_verificationdeadline'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    course_key = Column(String(255), nullable=False)
    deadline = Column(DateTime, nullable=False)
    deadline_is_explicit = Column(Integer, nullable=False)


class VerifyStudentVerificationstatus(Base):
    __tablename__ = 'verify_student_verificationstatus'

    id = Column(Integer, primary_key=True)
    status = Column(String(32), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    response = Column(String)
    error = Column(String)
    checkpoint_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class VideoConfigCoursehlsplaybackenabledflag(Base):
    __tablename__ = 'video_config_coursehlsplaybackenabledflag'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    course_id = Column(String(255), nullable=False)
    changed_by_id = Column(Integer)


class VideoConfigHlsplaybackenabledflag(Base):
    __tablename__ = 'video_config_hlsplaybackenabledflag'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    enabled_for_all_courses = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class WaffleFlag(Base):
    __tablename__ = 'waffle_flag'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    everyone = Column(Integer)
    percent = Column(Numeric(3, 1))
    testing = Column(Integer, nullable=False)
    superusers = Column(Integer, nullable=False)
    staff = Column(Integer, nullable=False)
    authenticated = Column(Integer, nullable=False)
    languages = Column(String, nullable=False)
    rollout = Column(Integer, nullable=False)
    note = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)


class WaffleFlagGroups(Base):
    __tablename__ = 'waffle_flag_groups'

    id = Column(Integer, primary_key=True)
    flag_id = Column(Integer, nullable=False)
    group_id = Column(Integer, nullable=False)


class WaffleFlagUsers(Base):
    __tablename__ = 'waffle_flag_users'

    id = Column(Integer, primary_key=True)
    flag_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)


class WaffleSample(Base):
    __tablename__ = 'waffle_sample'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    percent = Column(Numeric(4, 1), nullable=False)
    note = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)


class WaffleSwitch(Base):
    __tablename__ = 'waffle_switch'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    active = Column(Integer, nullable=False)
    note = Column(String, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)


class WaffleUtilsWaffleflagcourseoverridemodel(Base):
    __tablename__ = 'waffle_utils_waffleflagcourseoverridemodel'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    waffle_flag = Column(String(255), nullable=False)
    course_id = Column(String(255), nullable=False)
    override_choice = Column(String(3), nullable=False)
    changed_by_id = Column(Integer)


class WikiArticle(Base):
    __tablename__ = 'wiki_article'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    group_read = Column(Integer, nullable=False)
    group_write = Column(Integer, nullable=False)
    other_read = Column(Integer, nullable=False)
    other_write = Column(Integer, nullable=False)
    current_revision_id = Column(Integer)
    group_id = Column(Integer)
    owner_id = Column(Integer)


class WikiArticleforobject(Base):
    __tablename__ = 'wiki_articleforobject'

    id = Column(Integer, primary_key=True)
    object_id = Column(Integer, nullable=False)
    is_mptt = Column(Integer, nullable=False)
    article_id = Column(Integer, nullable=False)
    content_type_id = Column(Integer, nullable=False)


class WikiArticleplugin(Base):
    __tablename__ = 'wiki_articleplugin'

    id = Column(Integer, primary_key=True)
    deleted = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    article_id = Column(Integer, nullable=False)


class WikiArticlerevision(Base):
    __tablename__ = 'wiki_articlerevision'

    id = Column(Integer, primary_key=True)
    revision_number = Column(Integer, nullable=False)
    user_message = Column(String, nullable=False)
    automatic_log = Column(String, nullable=False)
    ip_address = Column(String(39))
    modified = Column(DateTime, nullable=False)
    created = Column(DateTime, nullable=False)
    deleted = Column(Integer, nullable=False)
    locked = Column(Integer, nullable=False)
    content = Column(String, nullable=False)
    title = Column(String(512), nullable=False)
    article_id = Column(Integer, nullable=False)
    previous_revision_id = Column(Integer)
    user_id = Column(Integer)


class WikiAttachment(Base):
    __tablename__ = 'wiki_attachment'

    reusableplugin_ptr_id = Column(Integer, primary_key=True)
    original_filename = Column(String(256))
    current_revision_id = Column(Integer)


class WikiAttachmentrevision(Base):
    __tablename__ = 'wiki_attachmentrevision'

    id = Column(Integer, primary_key=True)
    revision_number = Column(Integer, nullable=False)
    user_message = Column(String, nullable=False)
    automatic_log = Column(String, nullable=False)
    ip_address = Column(String(39))
    modified = Column(DateTime, nullable=False)
    created = Column(DateTime, nullable=False)
    deleted = Column(Integer, nullable=False)
    locked = Column(Integer, nullable=False)
    file = Column(String(100), nullable=False)
    description = Column(String, nullable=False)
    attachment_id = Column(Integer, nullable=False)
    previous_revision_id = Column(Integer)
    user_id = Column(Integer)


class WikiImage(Base):
    __tablename__ = 'wiki_image'

    revisionplugin_ptr_id = Column(Integer, primary_key=True)


class WikiImagerevision(Base):
    __tablename__ = 'wiki_imagerevision'

    revisionpluginrevision_ptr_id = Column(Integer, primary_key=True)
    image = Column(String(2000))
    width = Column(SmallInteger)
    height = Column(SmallInteger)


class WikiReusableplugin(Base):
    __tablename__ = 'wiki_reusableplugin'

    articleplugin_ptr_id = Column(Integer, primary_key=True)


class WikiReusablepluginArticles(Base):
    __tablename__ = 'wiki_reusableplugin_articles'

    id = Column(Integer, primary_key=True)
    reusableplugin_id = Column(Integer, nullable=False)
    article_id = Column(Integer, nullable=False)


t_wiki_revisionplugin = Table(
    'wiki_revisionplugin', metadata,
    Column('articleplugin_ptr_id', Integer, primary_key=True),
    Column('current_revision_id', Integer)
)


class WikiRevisionpluginrevision(Base):
    __tablename__ = 'wiki_revisionpluginrevision'

    id = Column(Integer, primary_key=True)
    revision_number = Column(Integer, nullable=False)
    user_message = Column(String, nullable=False)
    automatic_log = Column(String, nullable=False)
    ip_address = Column(String(39))
    modified = Column(DateTime, nullable=False)
    created = Column(DateTime, nullable=False)
    deleted = Column(Integer, nullable=False)
    locked = Column(Integer, nullable=False)
    plugin_id = Column(Integer, nullable=False)
    previous_revision_id = Column(Integer)
    user_id = Column(Integer)


t_wiki_simpleplugin = Table(
    'wiki_simpleplugin', metadata,
    Column('articleplugin_ptr_id', Integer, primary_key=True),
    Column('article_revision_id', Integer, nullable=False)
)


class WikiUrlpath(Base):
    __tablename__ = 'wiki_urlpath'

    id = Column(Integer, primary_key=True)
    slug = Column(String(255))
    lft = Column(Integer, nullable=False)
    rght = Column(Integer, nullable=False)
    tree_id = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)
    article_id = Column(Integer, nullable=False)
    parent_id = Column(Integer)
    site_id = Column(Integer, nullable=False)


class WorkflowAssessmentworkflow(Base):
    __tablename__ = 'workflow_assessmentworkflow'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    status = Column(String(100), nullable=False)
    status_changed = Column(DateTime, nullable=False)
    submission_uuid = Column(String(36), nullable=False)
    uuid = Column(String(36), nullable=False)
    course_id = Column(String(255), nullable=False)
    item_id = Column(String(255), nullable=False)


class WorkflowAssessmentworkflowcancellation(Base):
    __tablename__ = 'workflow_assessmentworkflowcancellation'

    id = Column(Integer, primary_key=True)
    comments = Column(String, nullable=False)
    cancelled_by_id = Column(String(40), nullable=False)
    created_at = Column(DateTime, nullable=False)
    workflow_id = Column(Integer, nullable=False)


class WorkflowAssessmentworkflowstep(Base):
    __tablename__ = 'workflow_assessmentworkflowstep'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    submitter_completed_at = Column(DateTime)
    assessment_completed_at = Column(DateTime)
    order_num = Column(Integer, nullable=False)
    workflow_id = Column(Integer, nullable=False)


class XblockConfigCourseeditltifieldsenabledflag(Base):
    __tablename__ = 'xblock_config_courseeditltifieldsenabledflag'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    course_id = Column(String(255), nullable=False)
    changed_by_id = Column(Integer)


class XblockConfigStudioconfig(Base):
    __tablename__ = 'xblock_config_studioconfig'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    disabled_blocks = Column(String, nullable=False)
    changed_by_id = Column(Integer)


class XblockDjangoXblockconfiguration(Base):
    __tablename__ = 'xblock_django_xblockconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    deprecated = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)


class XblockDjangoXblockstudioconfiguration(Base):
    __tablename__ = 'xblock_django_xblockstudioconfiguration'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    template = Column(String(255), nullable=False)
    support_level = Column(String(2), nullable=False)
    changed_by_id = Column(Integer)


class XblockDjangoXblockstudioconfigurationflag(Base):
    __tablename__ = 'xblock_django_xblockstudioconfigurationflag'

    id = Column(Integer, primary_key=True)
    change_date = Column(DateTime, nullable=False)
    enabled = Column(Integer, nullable=False)
    changed_by_id = Column(Integer)
