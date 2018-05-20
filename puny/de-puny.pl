#!/bin/env perl
use Net::LibIDN ':all';
#print idn_punycode_decode($ARGV[0],'utf-8');
print idn_to_unicode($ARGV[0],'utf-8') . "\n";
