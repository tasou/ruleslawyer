#!/bin/sh
zip -r "rules_lawyer.zip" ./ruleslawyer/*
aws --profile "$AWS_PROFILE" \
  lambda update-function-code \
  --function RulesLaywer \
  --zip-file fileb://rules_lawyer.zip
