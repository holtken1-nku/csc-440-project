#### TITLE

    lucky scarf - an association football API scraper

#### ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

#### ABOUT
    This application makes use of the football-data.org free public API to
    collect and store current data from several international association
    football (soccer) teams and competitions.  Data is maintained in
    JSON-compatible format to accommodate storage and handling for
    various purposes.

#### DIRECT DEPENDENCIES
    + Python, version 3.9.x (or newer)
    + MongoDB Community Edition, version 6.0 (or newer)
    + PyMongo, version 4.8.x (or newer)
    + A valid football-data.org API token

#### HOW TO USE THIS TOOL
    Before getting started, ensure that you have obtained a valid API token
    for football-data.org.  This token obviously constitutes sensitive data
    and should not be made public!  Contact Noah to obtain a copy of 
    env/constants.py and add this file to .gitignore.

    Run main.py to manually populate the database with current settings.
    If you prefer to run the script on a scheduled basis via crontab or
    a similar tool, ensure that extractions do not exceed the rate limit
    (10 calls/minute).  Additionally, certain measures have been taken to
    prevent duplicate entries in collection tables, but such measures are
    only applicable to MongoDB.

    Data is stored in MongoDB by default via src/load.py, however the
    output component can be modified to accomodate any JSON-compatible
    storage medium.  A database named "lucky_scarf" will be referenced
    by default, which contains one or more collection tables for various
    datasets.  These entities will be generated automatically if an
    existing resource is not found.

    MongoDB Compass is not required to manage the database, but it is
    highly recommended for ease-of-use while navigating data.

    football-data.org API reference documentation:
        https://docs.football-data.org/general/v4/index.html

#### ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~

#### COPYRIGHT & LICENSE
    Copyright © 2024 Northern Kentucky University.
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

#### CONTACT
    Noah Holtke (holtken1@mymail.nku.edu).
