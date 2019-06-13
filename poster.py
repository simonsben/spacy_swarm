from asyncio import gather, get_event_loop
from aiohttp import ClientSession
from utilities import load_config
from json import dumps, loads

endpoint = load_config()['endpoint']


def process_documents(documents):
    """ Run jobs synchronously """
    job_loop = get_event_loop()
    try:
        response = job_loop.run_until_complete(submit_jobs(documents))
    finally:
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

        return await gather(*jobs)


async def make_post(session, document):
    """ Make POST request """
    req_data = dumps({
        'text': document,
        'model': 'en'
    })

    async with session.post(endpoint, data=req_data) as response:
        res_data = await response.text()
        res = loads(res_data)

    return res['arcs']
