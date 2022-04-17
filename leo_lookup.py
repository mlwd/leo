
from bs4 import BeautifulSoup
import urllib.request
import sqlite3
import os
import sys

import leo_db

def leo_lookup(word_en):

  # Connect to data base.
  con = leo_db.leo_db_connect()
  if con == None:
    return None

  # Create data base cursor.
  cur = con.cursor()

  # Trying to create the table throws an error if it already exists.
  #cur.execute("create table dict (word_en, word_de)")

  # Note that word_en must be wrapped in a tuple to prevent the execute
  # function from treating the string as an iterable of characters.
  cur.execute("select word_de, n from dict where word_en=?", (word_en,))
  result = cur.fetchone()
  if result != None:
    # Select first and only entry from tuple word_de.
    n_lookups = result[1]
    print("Number of previous look-ups: %d" % n_lookups)
    # Increment number of lookups.
    n_lookups += 1
    cur.execute("update dict set n=? where word_en=?;", (n_lookups, word_en))
    con.commit()
    word_de = result[0]
    return word_de

  # Get HTML source from langenscheidt.com.
  path = "https://en.langenscheidt.com/english-german/" + word_en

  # The lookup may fail if the word does not exist or for other reasons.
  try:
    html = urllib.request.urlopen(path)
  except:
    return None

  # Convert HTML to BeautifulSoup.
  # The parser should be specified explicitly to prevent an error.
  soup = BeautifulSoup(html, "html.parser")

  # Find the first occurence of an HTML tag named "td" which has
  # an attribute "lang" with value "de".
  # Alternatively find_all would find all occurences.
  word_de_tag = soup.find("a", href="#sense-1.1.1")
  if word_de_tag == None:
    return None
  word_de_text = word_de_tag.get_text();
  word_de = word_de_text.strip();

  # Insert to local database.
  cur.execute("insert into dict values (?, ?, ?)", (word_en, word_de, 1))
  # Changes will lost unless they are committed!
  con.commit()
  return word_de
