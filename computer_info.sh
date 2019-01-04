#!/bin/bash
ifconfig | awk '{if($1=="inet")print"ip:"$2,"netmask:",$4"\t"}'
ifconfig | awk '{if($1=="ether")print"mac:"$2"\t"}'
hostname|awk '{print"hostname:",$1"\t"}'
free|awk '{if($1=="Mem:") print"mem_use:",$3/$2*100,"%""\t" }'
uptime|awk '{print"cpu_use:",$NF*100,"%""\t"}'
