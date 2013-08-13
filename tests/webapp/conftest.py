import json
from treeherder.webapp import wsgi
from tests.sample_data_generator import job_data
import pytest
from webtest.app import TestApp


@pytest.fixture
def webapp():
    """
    we can use this object to test calls to a wsgi application
    """
    return TestApp(wsgi.application)


@pytest.fixture
def job_sample():
    return job_data()


@pytest.fixture
def eleven_jobs_stored(jm):
    """stores a list of twenty job samples"""
    num_jobs = 11
    guids = ['myguid%s' % x for x in range(1, num_jobs + 1)]

    rh = 0
    pt = 0
    for guid in guids:
        job = job_data(job_guid=guid)
        job["revision_hash"] = rh
        job["sources"][0]["push_timestamp"] = pt
        jm.store_job_data(
            json.dumps(job),
            guid
        )
        pt += 1
        rh += 1


@pytest.fixture
def eleven_jobs_processed(initial_data, sample_data, jm):
    """stores and processes list of twenty job samples"""
    eleven_jobs_stored(jm)
    jm.process_objects(20)
