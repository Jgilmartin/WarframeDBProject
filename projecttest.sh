#!/bin/bash

db="warframeproject.sqlite"
rm -f ${db}
touch ${db}

sqlite3 ${db} < projectWarframe.sql