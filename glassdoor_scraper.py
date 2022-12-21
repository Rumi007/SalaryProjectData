#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 13:33:18 2022

@author: jalilkhan
"""

import glassdoor_scraper as gs
import pandas as pd

path ="/Users/jalilkhan/Documents/SalaryProjectData/chromedriver"

df = gs.get_jobs('data scientist', 7, False, path, 15)