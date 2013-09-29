#!/bin/bash

coverage run --source . -m py.test $@
coverage report
