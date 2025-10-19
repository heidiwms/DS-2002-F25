#!/bin/bash

read -p "Enter the TCG Card Set ID (e.g., base1, base4): " SET_ID

if [ -z "$SET_ID" ]; then
    echo "Error: Set ID cannot be empty." >&2
    exit 1
fi

echo "Fetching data for Pokémon TCG Set: $SET_ID ..."
sleep 2

if ! curl -s -L "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID" -o "card_set_lookup/${SET_ID}.json"; then
    echo "Error fetching data for $SET_ID. Please try again later." >&2
    exit 1
fi