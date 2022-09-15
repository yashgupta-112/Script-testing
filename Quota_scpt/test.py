SPACE=$(echo $space | awk '{print $18}' |  sed 's/[a-zA-Z]//g')  # will get disk size from this  {output = 284}
FILES=$(echo $space | awk '{print $21}' | sed 's/[a-zA-Z]//g' ) # get number of files in this command {output = 77}
SPACE_CHECK=$(echo $space | awk '{print $18}' | sed 's/[0-9]//g' )  # print number from string {output = G}
FILES_CHECK=$(echo $space | awk '{print $21}' | sed 's/[0-9]//g' ) # print number from string {output = k} small k