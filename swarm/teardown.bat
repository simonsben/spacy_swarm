:: Script to stop all containers and leave swarm
ECHO OFF

:: Stop containers
docker service rm spacy_swarm_spacy

:: Stop swarm
docker swarm leave --force

:: Leave open
PAUSE