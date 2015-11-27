# GLIBC Crypt

## Overview

Use this docker image to produce crypt(3) entries.

This can produce SHA-512 or standard DES ones.

## Usage

    # docker run -ti glibc-crypt
    Password: sdf
    $6$MP472zuEpfDM/1PN$eH5juHl7rN6wFZf2BqU8.Kdtdip3UFciVqJyVi7AHG.Y7ooGDnaZdEgJspMgAPxElHKlLQVPXE6d078LxaZWk0

    # docker run -ti glibc-crypt -d
    Password: sdf
    teVE9.DHdP6so
