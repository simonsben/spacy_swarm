:: Script to start a docker swarm and start the containers
ECHO OFF

:: Start the swarm
docker swarm init

:: Start the containers
docker stack deploy -c docker-compose.yml spacy_swarm

:: List service to ensure it launched
docker service ls

:: Leave window open
PAUSE