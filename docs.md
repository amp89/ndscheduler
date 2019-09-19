

# ndscheduler.core.scheduler_manager_test


##### Imports
- builtins.str
- tornado.testing
- ndscheduler.utils
- ndscheduler.core.scheduler_manager

#### ndscheduler.core.scheduler_manager_test.SchedulerManagerTest

##### Inherits from
- tornado.testing.AsyncTestCase

##### Attributes
- self.scheduler

#### ndscheduler.core.scheduler_manager_test.SchedulerManagerTest.setUp

##### Arguments
- *args
- **kwargs

#### ndscheduler.core.scheduler_manager_test.SchedulerManagerTest.tearDown

##### Arguments
- *args
- **kwargs

#### ndscheduler.core.scheduler_manager_test.SchedulerManagerTest.test_add_job_get_job

##### Annotations
- @tornado.testing.gen_test

#### ndscheduler.core.scheduler_manager_test.SchedulerManagerTest.test_add_job_modify_job

##### Annotations
- @tornado.testing.gen_test

# ndscheduler.core.scheduler_manager


##### Imports
- logging
- apscheduler.executors.pool
- ndscheduler.settings
- ndscheduler.utils

#### ndscheduler.core.scheduler_manager.SchedulerManager:

##### Attributes
- self.sched

#### ndscheduler.core.scheduler_manager.SchedulerManager:.get_instance

##### Arguments
- cls

##### Returns
- cls.instance

##### Annotations
- @classmethod

#### ndscheduler.core.scheduler_manager.SchedulerManager:.__init__

#### ndscheduler.core.scheduler_manager.SchedulerManager:.get_datastore

##### Returns
- self.sched._lookup_jobstore('default')

#### ndscheduler.core.scheduler_manager.SchedulerManager:.start

#### ndscheduler.core.scheduler_manager.SchedulerManager:.stop

#### ndscheduler.core.scheduler_manager.SchedulerManager:.add_job

##### Arguments
- job_class_string
- name
- pub_args=None

##### Returns
- self.sched.add_scheduler_job(job_class_string, name, pub_args, month, day_of_week,

#### ndscheduler.core.scheduler_manager.SchedulerManager:.pause_job

##### Arguments
- job_id

#### ndscheduler.core.scheduler_manager.SchedulerManager:.get_job

##### Arguments
- job_id

##### Returns
- self.sched.get_job(job_id)

#### ndscheduler.core.scheduler_manager.SchedulerManager:.get_jobs

##### Returns
- self.sched.get_jobs()

#### ndscheduler.core.scheduler_manager.SchedulerManager:.get_job_task_class

##### Arguments
- job

##### Returns
- job.args[0]

#### ndscheduler.core.scheduler_manager.SchedulerManager:.remove_job

##### Arguments
- job_id

#### ndscheduler.core.scheduler_manager.SchedulerManager:.resume_job

##### Arguments
- job_id

#### ndscheduler.core.scheduler_manager.SchedulerManager:.modify_job

##### Arguments
- job_id
- **kwargs

# ndscheduler.core.scheduler.base_test


##### Imports
- mock
- unittest
- ndscheduler.core.scheduler_manager

#### ndscheduler.core.scheduler.base_test.SingletonSchedulerTest

##### Inherits from
- unittest.TestCase

#### ndscheduler.core.scheduler.base_test.SingletonSchedulerTest.test_is_okay_to_run

#### ndscheduler.core.scheduler.base_test.SingletonSchedulerTest.test_is_not_okay_to_run

# ndscheduler.core.scheduler.base


##### Imports
- logging
- apscheduler.schedulers.tornado.as.apscheduler_tornado
- ndscheduler.constants
- ndscheduler.job
- ndscheduler.settings
- ndscheduler.utils

#### ndscheduler.core.scheduler.base.SingletonScheduler 

##### Inherits from
- apscheduler_tornado.TornadoScheduler

##### Attributes
- self.DEFAULT_WAIT_SECONDS

#### ndscheduler.core.scheduler.base.SingletonScheduler .is_okay_to_run

##### Arguments
- cls
- database

##### Returns
- True

##### Annotations
- @classmethod

#### ndscheduler.core.scheduler.base.SingletonScheduler .run_job

##### Arguments
- cls
- job_class_path
- job_id
- *args
- **kwargs

##### Returns
- None
- execution_id

##### Annotations
- @classmethod

#### ndscheduler.core.scheduler.base.SingletonScheduler .run_scheduler_job

##### Arguments
- cls
- job_class
- job_id
- execution_id
- *args
- **kwargs

##### Annotations
- @classmethod

#### ndscheduler.core.scheduler.base.SingletonScheduler .add_scheduler_job

##### Arguments
- job_class_string
- name
- pub_args=None

##### Returns
- job_id

#### ndscheduler.core.scheduler.base.SingletonScheduler .modify_scheduler_job

##### Arguments
- job_id
- **kwargs

#### ndscheduler.core.scheduler.base.SingletonScheduler ._process_jobs

##### Returns
- super(apscheduler_tornado.TornadoScheduler, self)._process_jobs()
- self.DEFAULT_WAIT_SECONDS

# ndscheduler.core.datastore.providers.base_test


##### Imports
- datetime
- unittest
- ndscheduler.constants
- ndscheduler.core.datastore.providers.base
- apscheduler.schedulers.blocking.BlockingScheduler

#### ndscheduler.core.datastore.providers.base_test.SimpleDatastore

##### Inherits from
- base.DatastoreBase

#### ndscheduler.core.datastore.providers.base_test.SimpleDatastore.get_db_url

##### Arguments
- cls

##### Returns
- 'sqlite:///'

##### Annotations
- @classmethod

#### ndscheduler.core.datastore.providers.base_test.SimpleDatastore.get_time_isoformat_from_db

##### Arguments
- time_object

##### Returns
- time_object

#### ndscheduler.core.datastore.providers.base_test.DatastoreBaseTest

##### Inherits from
- unittest.TestCase

##### Attributes
- self.store

#### ndscheduler.core.datastore.providers.base_test.DatastoreBaseTest.setUp

#### ndscheduler.core.datastore.providers.base_test.DatastoreBaseTest.test_add_execution_get_execution

#### ndscheduler.core.datastore.providers.base_test.DatastoreBaseTest.test_update_execution_get_execution

#### ndscheduler.core.datastore.providers.base_test.DatastoreBaseTest.test_get_executions_by_time_interval

#### ndscheduler.core.datastore.providers.base_test.DatastoreBaseTest.test_add_aduit_log_get_audit_logs

# ndscheduler.core.datastore.providers.postgresql


##### Imports
- ndscheduler.settings
- ndscheduler.core.datastore.providers.base

#### ndscheduler.core.datastore.providers.postgresql.DatastorePostgresql

##### Inherits from
- base.DatastoreBase

#### ndscheduler.core.datastore.providers.postgresql.DatastorePostgresql.get_db_url

##### Arguments
- cls

##### Returns
- 'postgresql://%s:%s@%s:%d/%s?sslmode=%s' % (

##### Annotations
- @classmethod

# ndscheduler.core.datastore.providers.sqlite


##### Imports
- datetime
- pytz
- ndscheduler.settings
- ndscheduler.core.datastore.providers.base

#### ndscheduler.core.datastore.providers.sqlite.DatastoreSqlite

##### Inherits from
- base.DatastoreBase

#### ndscheduler.core.datastore.providers.sqlite.DatastoreSqlite.get_db_url

##### Arguments
- cls

##### Returns
- 'sqlite:///' + file_path

##### Annotations
- @classmethod

#### ndscheduler.core.datastore.providers.sqlite.DatastoreSqlite.get_time_isoformat_from_db

##### Arguments
- time_object

##### Returns
- date.isoformat()

# ndscheduler.core.datastore.providers.base


##### Imports
- dateutil.parser
- dateutil.tz
- apscheduler.jobstores.sqlalchemy.as.sched_sqlalchemy
- sqlalchemy.select
- sqlalchemy.desc
- ndscheduler.constants
- ndscheduler.settings
- ndscheduler.utils
- ndscheduler.core.datastore.tables

#### ndscheduler.core.datastore.providers.base.DatastoreBase

##### Inherits from
- sched_sqlalchemy.SQLAlchemyJobStore

#### ndscheduler.core.datastore.providers.base.DatastoreBase.get_instance

##### Arguments
- cls

##### Returns
- cls.instance

##### Annotations
- @classmethod

#### ndscheduler.core.datastore.providers.base.DatastoreBase.destroy_instance

##### Arguments
- cls

##### Annotations
- @classmethod

#### ndscheduler.core.datastore.providers.base.DatastoreBase.get_db_url

##### Arguments
- cls

##### Exceptions
- NotImplementedError('Please implement this function.')

##### Annotations
- @classmethod

#### ndscheduler.core.datastore.providers.base.DatastoreBase.add_execution

##### Arguments
- execution_id
- job_id
- state
- **kwargs

#### ndscheduler.core.datastore.providers.base.DatastoreBase.get_execution

##### Arguments
- execution_id

##### Returns
- self._build_execution(row)

#### ndscheduler.core.datastore.providers.base.DatastoreBase.update_execution

##### Arguments
- execution_id
- **kwargs

#### ndscheduler.core.datastore.providers.base.DatastoreBase._build_execution

##### Arguments
- row

##### Returns
- return_json

#### ndscheduler.core.datastore.providers.base.DatastoreBase.get_time_isoformat_from_db

##### Arguments
- time_object

##### Returns
- time_object.isoformat()

#### ndscheduler.core.datastore.providers.base.DatastoreBase.get_executions

##### Arguments
- time_range_start
- time_range_end

##### Returns
- return_json

#### ndscheduler.core.datastore.providers.base.DatastoreBase.add_audit_log

##### Arguments
- job_id
- job_name
- event
- user=''
- description=''
- **kwargs

#### ndscheduler.core.datastore.providers.base.DatastoreBase.get_audit_logs

##### Arguments
- time_range_start
- time_range_end

##### Returns
- return_json

#### ndscheduler.core.datastore.providers.base.DatastoreBase._build_audit_log

##### Arguments
- row

##### Returns
- return_dict

# ndscheduler.core.datastore.providers.mysql


##### Imports
- ndscheduler.settings
- ndscheduler.core.datastore.providers.base

#### ndscheduler.core.datastore.providers.mysql.DatastoreMysql

##### Inherits from
- base.DatastoreBase

#### ndscheduler.core.datastore.providers.mysql.DatastoreMysql.get_db_url

##### Arguments
- cls

##### Returns
- 'mysql+pymysql://%s:%s@%s:%d/%s' % (

##### Annotations
- @classmethod

# ndscheduler.core.datastore.tables


##### Imports
- sqlalchemy
- ndscheduler.settings
- ndscheduler.utils

# ndscheduler.version


# ndscheduler.utils_test


##### Imports
- unittest
- ndscheduler.utils

#### ndscheduler.utils_test.UtilsTest

##### Inherits from
- unittest.TestCase

#### ndscheduler.utils_test.UtilsTest.test_class_import_from_path

# ndscheduler.job


##### Imports
- json
- logging
- os
- socket
- ndscheduler.constants
- ndscheduler.utils
- ndscheduler.core.scheduler_manager

#### ndscheduler.job.JobBase:

##### Attributes
- self.job_id
- self.execution_id

#### ndscheduler.job.JobBase:.__init__

##### Arguments
- job_id
- execution_id

#### ndscheduler.job.JobBase:.create_test_instance

##### Arguments
- cls

##### Annotations
- @classmethod

#### ndscheduler.job.JobBase:.get_scheduled_description

##### Arguments
- cls

##### Returns
- 'hostname: %s | pid: %s' % (hostname, pid)

##### Annotations
- @classmethod

#### ndscheduler.job.JobBase:.get_scheduled_error_description

##### Arguments
- cls

##### Returns
- 'hostname: %s | pid: %s' % (hostname, pid)

##### Annotations
- @classmethod

#### ndscheduler.job.JobBase:.get_running_description

##### Arguments
- cls

##### Returns
- 'hostname: %s | pid: %s' % (hostname, pid)

##### Annotations
- @classmethod

#### ndscheduler.job.JobBase:.get_failed_description

##### Arguments
- cls

##### Returns
- 'hostname: %s | pid: %s' % (hostname, pid)

##### Annotations
- @classmethod

#### ndscheduler.job.JobBase:.get_succeeded_description

##### Arguments
- cls
- result=None

##### Returns
- 'hostname: %s | pid: %s' % (hostname, pid)

##### Annotations
- @classmethod

#### ndscheduler.job.JobBase:.get_scheduled_error_result

##### Arguments
- cls

##### Returns
- utils.get_stacktrace()

##### Annotations
- @classmethod

#### ndscheduler.job.JobBase:.get_failed_result

##### Arguments
- cls

##### Returns
- utils.get_stacktrace()

##### Annotations
- @classmethod

#### ndscheduler.job.JobBase:.meta_info

##### Arguments
- cls

##### Returns
- {

##### Annotations
- @classmethod

#### ndscheduler.job.JobBase:.run_job

##### Arguments
- cls
- job_id
- execution_id
- *args
- **kwargs

##### Annotations
- @classmethod

#### ndscheduler.job.JobBase:.run

##### Arguments
- *args
- **kwargs

##### Exceptions
- NotImplementedError('Please implement this function')

# ndscheduler.constants


# ndscheduler.default_settings_test


# ndscheduler.server.server


##### Imports
- logging
- signal
- sys
- tornado
- ndscheduler.settings
- ndscheduler.core.scheduler_manager
- ndscheduler.server.handlers.audit_logs
- ndscheduler.server.handlers.executions
- ndscheduler.server.handlers.index
- ndscheduler.server.handlers.jobs

#### ndscheduler.server.server.SchedulerServer:

##### Attributes
- self.scheduler_manager
- self.tornado_settings
- self.VERSION,
- self.VERSION,
- self.VERSION,
- self.VERSION,
- self.VERSION,
- self.application

#### ndscheduler.server.server.SchedulerServer:.__init__

##### Arguments
- scheduler_instance

#### ndscheduler.server.server.SchedulerServer:.start_scheduler

#### ndscheduler.server.server.SchedulerServer:.post_scheduler_start

#### ndscheduler.server.server.SchedulerServer:.stop_scheduler

#### ndscheduler.server.server.SchedulerServer:.post_scheduler_stop

#### ndscheduler.server.server.SchedulerServer:.signal_handler

##### Arguments
- cls
- signal
- frame

##### Annotations
- @classmethod

#### ndscheduler.server.server.SchedulerServer:.run

##### Arguments
- cls

##### Annotations
- @classmethod

# ndscheduler.server.handlers.executions


##### Imports
- datetime.datetime
- datetime.timedelta
- tornado.web
- tornado.gen
- ndscheduler.constants
- ndscheduler.utils
- ndscheduler.core.scheduler.base.as.scheduler_base
- ndscheduler.server.handlers.base

#### ndscheduler.server.handlers.executions.Handler

##### Inherits from
- base.BaseHandler

##### Attributes
- self.username,

#### ndscheduler.server.handlers.executions.Handler._get_execution

##### Arguments
- execution_id

##### Returns
- {'error': 'Execution not found: %s' % execution_id}
- execution

#### ndscheduler.server.handlers.executions.Handler.get_execution

##### Arguments
- execution_id

##### Returns
- self._get_execution(execution_id)

##### Annotations
- @tornado.concurrent.run_on_executor

#### ndscheduler.server.handlers.executions.Handler.get_execution_yield

##### Arguments
- execution_id

##### Annotations
- @tornado.gen.engine

#### ndscheduler.server.handlers.executions.Handler._get_executions

##### Returns
- executions

#### ndscheduler.server.handlers.executions.Handler.get_executions

##### Returns
- self._get_executions()

##### Annotations
- @tornado.concurrent.run_on_executor

#### ndscheduler.server.handlers.executions.Handler.get_executions_yield

##### Annotations
- @tornado.gen.engine

#### ndscheduler.server.handlers.executions.Handler.get

##### Arguments
- execution_id=None

##### Annotations
- @tornado.gen.engine
- @tornado.web.asynchronous
- @tornado.web.removeslash

#### ndscheduler.server.handlers.executions.Handler._run_job

##### Arguments
- job_id

##### Returns
- {'error': 'Job not found: %s' % job_id}
- response

#### ndscheduler.server.handlers.executions.Handler.run_job

##### Arguments
- job_id

##### Returns
- self._run_job(job_id)

##### Annotations
- @tornado.concurrent.run_on_executor

#### ndscheduler.server.handlers.executions.Handler.run_job_yield

##### Arguments
- job_id

##### Annotations
- @tornado.gen.engine

#### ndscheduler.server.handlers.executions.Handler.post

##### Arguments
- job_id

##### Annotations
- @tornado.gen.engine
- @tornado.web.asynchronous
- @tornado.web.removeslash

#### ndscheduler.server.handlers.executions.Handler.delete

##### Arguments
- job_id

##### Exceptions
- tornado.web.HTTPError(501, 'Not implemented yet.')

##### Annotations
- @tornado.web.removeslash

# ndscheduler.server.handlers.index


##### Imports
- json
- ndscheduler.settings
- ndscheduler.utils
- ndscheduler.server.handlers.base

#### ndscheduler.server.handlers.index.Handler

##### Inherits from
- base.BaseHandler

#### ndscheduler.server.handlers.index.Handler.get

# ndscheduler.server.handlers.jobs_test


##### Imports
- json
- tornado.testing
- ndscheduler.utils
- ndscheduler.core.scheduler_manager
- ndscheduler.server.server
- ndscheduler.server.handlers.jobs

#### ndscheduler.server.handlers.jobs_test.mock_get_jobs_yield

#### ndscheduler.server.handlers.jobs_test.mock_get_job_yield

##### Arguments
- job_id

#### ndscheduler.server.handlers.jobs_test.mock_delete_job_yield

##### Arguments
- job_id

#### ndscheduler.server.handlers.jobs_test.mock_modify_job_yield

##### Arguments
- job_id

#### ndscheduler.server.handlers.jobs_test.JobsTest

##### Inherits from
- tornado.testing.AsyncHTTPTestCase

##### Attributes
- self.JOBS_URL
- self.old_get_jobs_yield
- self.old_get_job_yield
- self.old_delete_job_yield
- self.old_modify_job_yield
- self.old_get_jobs_yield
- self.old_get_job_yield
- self.old_delete_job_yield
- self.old_modify_job_yield
- self.scheduler
- self.server
- self.server.application

#### ndscheduler.server.handlers.jobs_test.JobsTest.setUp

##### Arguments
- *args
- **kwargs

#### ndscheduler.server.handlers.jobs_test.JobsTest.tearDown

##### Arguments
- *args
- **kwargs

#### ndscheduler.server.handlers.jobs_test.JobsTest.get_app

#### ndscheduler.server.handlers.jobs_test.JobsTest.test_add_job_success

#### ndscheduler.server.handlers.jobs_test.JobsTest.test_add_job_failed

#### ndscheduler.server.handlers.jobs_test.JobsTest.test_pause_resume_job

#### ndscheduler.server.handlers.jobs_test.JobsTest.test_get_jobs

#### ndscheduler.server.handlers.jobs_test.JobsTest.test_delete_job

#### ndscheduler.server.handlers.jobs_test.JobsTest.test_modify_job

# ndscheduler.server.handlers.jobs


##### Imports
- json
- tornado.concurrent
- tornado.gen
- tornado.web
- ndscheduler.constants
- ndscheduler.utils
- ndscheduler.server.handlers.base

#### ndscheduler.server.handlers.jobs.Handler

##### Inherits from
- base.BaseHandler

##### Attributes
- self.json_args['name'],
- self.username,
- self.username,
- self.json_args:
- self.json_args:

#### ndscheduler.server.handlers.jobs.Handler._get_jobs

##### Returns
- {'jobs': return_json}

#### ndscheduler.server.handlers.jobs.Handler._build_job_dict

##### Arguments
- job

##### Returns
- return_dict

#### ndscheduler.server.handlers.jobs.Handler.get_jobs

##### Returns
- self._get_jobs()

##### Annotations
- @tornado.concurrent.run_on_executor

#### ndscheduler.server.handlers.jobs.Handler.get_jobs_yield

##### Annotations
- @tornado.gen.engine

#### ndscheduler.server.handlers.jobs.Handler._get_job

##### Arguments
- job_id

##### Returns
- {'error': 'Job not found: %s' % job_id}
- self._build_job_dict(job)

#### ndscheduler.server.handlers.jobs.Handler.get_job

##### Arguments
- job_id

##### Returns
- self._get_job(job_id)

##### Annotations
- @tornado.concurrent.run_on_executor

#### ndscheduler.server.handlers.jobs.Handler.get_job_yield

##### Arguments
- job_id

##### Annotations
- @tornado.gen.engine

#### ndscheduler.server.handlers.jobs.Handler.get

##### Arguments
- job_id=None

##### Annotations
- @tornado.gen.engine
- @tornado.web.asynchronous
- @tornado.web.removeslash

#### ndscheduler.server.handlers.jobs.Handler.post

##### Annotations
- @tornado.web.removeslash

#### ndscheduler.server.handlers.jobs.Handler._delete_job

##### Arguments
- job_id

#### ndscheduler.server.handlers.jobs.Handler.delete_job

##### Arguments
- job_id

##### Annotations
- @tornado.concurrent.run_on_executor

#### ndscheduler.server.handlers.jobs.Handler.delete_job_yield

##### Arguments
- job_id

##### Annotations
- @tornado.gen.engine

#### ndscheduler.server.handlers.jobs.Handler.delete

##### Arguments
- job_id

##### Annotations
- @tornado.gen.engine
- @tornado.web.asynchronous
- @tornado.web.removeslash

#### ndscheduler.server.handlers.jobs.Handler._generate_description_for_item

##### Arguments
- old_job
- new_job
- item

##### Returns
- ('<b>%s</b>: <font color="red">%s</font> =>'
- ''

#### ndscheduler.server.handlers.jobs.Handler._generate_description_for_modify

##### Arguments
- old_job
- new_job

##### Returns
- description

#### ndscheduler.server.handlers.jobs.Handler._modify_job

##### Arguments
- job_id

#### ndscheduler.server.handlers.jobs.Handler.modify_job

##### Arguments
- job_id

##### Annotations
- @tornado.concurrent.run_on_executor

#### ndscheduler.server.handlers.jobs.Handler.modify_job_yield

##### Arguments
- job_id

##### Annotations
- @tornado.gen.engine

#### ndscheduler.server.handlers.jobs.Handler.put

##### Arguments
- job_id

##### Annotations
- @tornado.gen.engine
- @tornado.web.asynchronous
- @tornado.web.removeslash

#### ndscheduler.server.handlers.jobs.Handler.patch

##### Arguments
- job_id

##### Annotations
- @tornado.web.removeslash

#### ndscheduler.server.handlers.jobs.Handler.options

##### Arguments
- job_id

##### Annotations
- @tornado.web.removeslash

#### ndscheduler.server.handlers.jobs.Handler._validate_post_data

##### Exceptions
- tornado.web.HTTPError(400, reason='Require this parameter: %s' % field)
- tornado.web.HTTPError(400, reason=('Require at least one of following parameters:'

# ndscheduler.server.handlers.audit_logs


##### Imports
- datetime.datetime
- datetime.timedelta
- tornado.web
- tornado.gen
- ndscheduler.server.handlers.base

#### ndscheduler.server.handlers.audit_logs.Handler

##### Inherits from
- base.BaseHandler

#### ndscheduler.server.handlers.audit_logs.Handler._get_logs

##### Returns
- logs

#### ndscheduler.server.handlers.audit_logs.Handler.get_logs

##### Returns
- self._get_logs()

##### Annotations
- @tornado.concurrent.run_on_executor

#### ndscheduler.server.handlers.audit_logs.Handler.get_logs_yield

##### Annotations
- @tornado.gen.engine

#### ndscheduler.server.handlers.audit_logs.Handler.get

##### Annotations
- @tornado.gen.engine
- @tornado.web.asynchronous
- @tornado.web.removeslash

# ndscheduler.server.handlers.base


##### Imports
- json
- concurrent.futures
- tornado.ioloop
- tornado.web
- ndscheduler.settings

#### ndscheduler.server.handlers.base.MainHandler

##### Inherits from
- tornado.web.RequestHandler

#### ndscheduler.server.handlers.base.MainHandler.get

#### ndscheduler.server.handlers.base.BaseHandler

##### Inherits from
- tornado.web.RequestHandler

##### Attributes
- self.json_args
- self.json_args
- self.username
- self.scheduler_manager
- self.application.settings['scheduler_manager']
- self.datastore

#### ndscheduler.server.handlers.base.BaseHandler.prepare

#### ndscheduler.server.handlers.base.BaseHandler.get_username

##### Returns
- ''

# ndscheduler.server.handlers.executions_test


##### Imports
- datetime
- json
- tornado.testing
- ndscheduler.constants
- ndscheduler.core.scheduler_manager
- ndscheduler.server.server
- ndscheduler.server.handlers.executions

#### ndscheduler.server.handlers.executions_test.mock_get_executions_yield

#### ndscheduler.server.handlers.executions_test.mock_get_execution_yield

##### Arguments
- execution_id

#### ndscheduler.server.handlers.executions_test.ExecutionsTest

##### Inherits from
- tornado.testing.AsyncHTTPTestCase

##### Attributes
- self.EXECUTIONS_URL
- self.old_get_executions_yield
- self.old_get_execution_yield
- self.old_get_executions_yield
- self.old_get_execution_yield
- self.scheduler
- self.server
- self.server.application

#### ndscheduler.server.handlers.executions_test.ExecutionsTest.setUp

##### Arguments
- *args
- **kwargs

#### ndscheduler.server.handlers.executions_test.ExecutionsTest.tearDown

##### Arguments
- *args
- **kwargs

#### ndscheduler.server.handlers.executions_test.ExecutionsTest.get_app

##### Returns
- self.server.application

#### ndscheduler.server.handlers.executions_test.ExecutionsTest.test_get_execution

#### ndscheduler.server.handlers.executions_test.ExecutionsTest.test_get_execution1

# ndscheduler.default_settings


##### Imports
- logging
- os

# ndscheduler.utils


##### Imports
- builtins.str
- datetime
- lib
- logging
- glob
- os
- pytz
- sys
- traceback
- uuid
- ndscheduler.settings

#### ndscheduler.utils.import_from_path

##### Arguments
- path

##### Returns
- getattr(module, components[-1])

#### ndscheduler.utils.get_current_datetime

##### Returns
- datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

#### ndscheduler.utils.generate_uuid

##### Returns
- uuid.uuid1().hex

#### ndscheduler.utils.get_job_name

##### Arguments
- job

##### Returns
- job.args[0]

#### ndscheduler.utils.get_job_args

##### Arguments
- job

##### Returns
- job.args[2:]

#### ndscheduler.utils.get_job_kwargs

##### Arguments
- job

##### Returns
- job.kwargs

#### ndscheduler.utils.get_cron_strings

##### Arguments
- job

##### Returns
- {

#### ndscheduler.utils.get_datastore_instance

##### Returns
- database_class.get_instance()

#### ndscheduler.utils.get_stacktrace

#### ndscheduler.utils.get_all_available_jobs

##### Returns
- results

# ndscheduler.auto_document_a


##### Imports
- scandir
- sys
- os
- re

#### ndscheduler.auto_document_a.get_annotation_list

##### Arguments
- line_list
- idx

##### Returns
- annotation_list

#### ndscheduler.auto_document_a.get_f_args

##### Arguments
- line

##### Returns
- []
- arg_list

#### ndscheduler.auto_document_a.get_thingy

##### Arguments
- type_of_thingy
- line_list
- idx
- pause_characters=False

#### ndscheduler.auto_document_a.get_attributes

##### Arguments
- line_list
- idx

##### Returns
- attr_list

#### ndscheduler.auto_document_a.get_deps

##### Arguments
- line_list
- idx

##### Returns
- None
- return_list

#### ndscheduler.auto_document_a.get_import_list

##### Arguments
- line_list

##### Returns
- imports

#### ndscheduler.auto_document_a.write_lines

##### Arguments
- file_obj
- header
- iter_list

#### ndscheduler.auto_document_a.write_data

##### Arguments
- file_obj
- current_module=None
- dep_list=None
- annotation_list=None
- current_class=None
- \

#### ndscheduler.auto_document_a.write_import_list

##### Arguments
- file_obj
- import_list

#### ndscheduler.auto_document_a.document_module

##### Arguments
- module_path
- file_obj

#### ndscheduler.auto_document_a.")[1].split

##### Arguments
- "def "

#### ndscheduler.auto_document_a." in line:

##### Arguments
- " "

#### ndscheduler.auto_document_a.")[1].split

##### Arguments
- "def "

#### ndscheduler.auto_document_a.scany_stuff

##### Arguments
- scan_path
- file_obj

# setu


##### Imports
- multiprocessing  # To make python setup.py test happy
- os
- shutil
- subprocess
- distutils.command.clean.clean
- setuptools.find_packages
- setuptools.setup

#### setu.CleanHook

##### Inherits from
- clean

#### setu.CleanHook.run

#### setu.CleanHook.maybe_rm

##### Arguments
- path