#!/bin/bash

db="warframeDB.sqlite"
rm -f ${db}
touch ${db}

sqlite3 ${db} < projectWarframe.sql