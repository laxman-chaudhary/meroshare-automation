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

	elif [[ $line =~ ^[0-9]+$ ]]; then
        # Extract "Applied Kitta" value if the line contains only digits
        applied_kitta="$line"
    fi

   # Check if all the necessary information has been collected
    if [[ -n "$share_type" && -n "$share_group" && -n "$company" && -n "$email" && -n "$date" && -n "$applied_kitta" ]]; then
        # Prepare the message with proper formatting (using Markdown for bold)
   message="Dear *$user_name*,
   Share Applied Sucessfully: *$applied_kitta किट्टा*

   *Type:*  \`$share_type\`
   *Group:* \`$share_group\`
   *Applied Kitta:* \`$applied_kitta\`
   *Email:* \`$email\`
   *Applied Date:* \`$date\`
   *Company Name:* \`$company\`

   _*Please maintain minimum banalce in your Account_"
        
        # Send the message using curl
        curl -s -X POST "https://api.telegram.org/bot$secret_key/sendMessage" -d "chat_id=$chat_id" -d "text=$message" -d "parse_mode=Markdown"
   
	# Reset variables for the next entry
        share_type=""
        share_group=""
        company=""
        email=""
        date=""
        applied_kitta=""

    fi
done < ../meroshare.log
