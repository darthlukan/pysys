Command: storeEval

Target: var d=new Date(); ((d.getMonth()+1))+'/'+ (d.getDate()) +'/'+(d.getFullYear());

Value: current_date
then to use that 

Command: type
Target: approval_expires
Value: ${current_date}
