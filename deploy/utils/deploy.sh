#!/usr/bin/env bash

##
## Workflow for deploying docker containers.
##

dc="docker-compose"

# Set ENV variable PROD for Production environment.
#
# >> export PROD=1
#
# Unset variable PROD for Development environment.
#
# >> unset PROD

if [[ $PROD ]]
then
    # Pull latest changes.
    dc="docker-compose -f docker-compose-prod.yml"
    $dc pull
fi

# Stop existing containers.
$dc stop -t 1

# Remove existing volumes.
$dc rm -fv

# Recreate and start containers.
$dc up -d
