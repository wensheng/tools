#!/bin/env perl
use Net::LibIDN ':all';
#print idn_punycode_encode($ARGV[0],'utf-8');
print idn_to_ascii($ARGV[0],'utf-8') . "\n";
