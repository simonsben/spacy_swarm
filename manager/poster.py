from asyncio import gather, get_event_loop
from aiohttp import ClientSession
from manager.utilities import load_config
from json import dumps, loads, JSONDecodeError

endpoint = load_config()['endpoint']


def process_documents(documents, job_loop=None):
    """ Run jobs synchronously """
    job_loop = get_event_loop() if job_loop is None else job_loop
    response = job_loop.run_until_complete(submit_jobs(documents))

    if job_loop is None:
        job_loop.close()

    return response


async def submit_jobs(documents):
    """ Process documents on the swarm """
    async with ClientSession() as session:
        jobs = []
        for document in documents:
            jobs.append(
                make_post(session, document)
            )
        result = await gather(*jobs)

    return result


async def make_post(session, document):
    """ Make POST request """
    req_data = dumps({
        'text': document,
        'model': 'en'
    })

    async with session.post(endpoint, data=req_data) as response:
        res_data = await response.text()

        try:
            res = loads(res_data)
        except JSONDecodeError:
            return []

    return res['arcs']

