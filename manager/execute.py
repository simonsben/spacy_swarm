from manager.poster import process_documents
from time import time
from matplotlib.pyplot import subplots, title, show
from asyncio import get_event_loop


set_sizes, set_times = [], []
job_loop = get_event_loop()
for num_docs in range(100, 300, 100):
    # Define document set
    documents = ['Hello there, how is it going? My day is going quite well actually! Sounds swell..'] * num_docs

    # Process documents
    start = time()
    processed_docs = process_documents(documents, job_loop=job_loop)
    end = time()

    # Save execution time
    set_sizes.append(num_docs)
    set_times.append(end - start)

    print('Finished', num_docs, 'in', (end - start) / num_docs)

job_loop.close()
print('Done, plotting times')

# Plot execution time
fig, ax = subplots()
ax.scatter(set_sizes, set_times)

title('Time to process documents')
ax.set_xlabel('Number of documents')
ax.set_ylabel('Average time per document (s)')

show()
