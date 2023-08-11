#!/bin/bash
#Author: Alex
#Description: This script notify user via Telegram message when share is applied sucessfully.


source "$(dirname "${BASH_SOURCE[0]}")/.token"

while IFS= read -r line; do
    if [[ $line != *"no share issued"* && $line != *"Debentures"* && $line == *"IPO"* && $line == *"Ordinary Shares"* ]]; then
        # Extract information using grep and sed
        share_type=$(echo "$line" | sed -nE "s/.*'share_type': '([^']+)'.*/\1/p")
        share_group=$(echo "$line" | sed -nE "s/.*'share group': '([^']+)'.*/\1/p")
        company=$(echo "$line" | sed -nE "s/.*'company': '([^']+)'.*/\1/p")
        email=$(echo "$line" | sed -nE "s/.*'email': '([^']+)'.*/\1/p")
        date=$(echo "$line" | sed -nE "s/.*'applied_time': '([^']+)'.*/\1/p")

# Prepare the message with proper formatting (using Markdown for bold)
   message="Dear *$user_name*,
   Share Applied Sucessfully
   *Type:*  \`$share_type\`
   *Group:* \`$share_group\`
   *Company Name:* \`$company\` 
   *Email:* \`$email\`
   *Applied Date:* \`$date\`

   _*Please maintain minimum banalce in your Account_"
        
        # Send the message using curl
        curl -s -X POST "https://api.telegram.org/bot$secret_key/sendMessage" -d "chat_id=$chat_id" -d "text=$message" -d "parse_mode=Markdown"
    fi
done < ../meroshare.log
