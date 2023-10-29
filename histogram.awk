# histogram.awk

BEGIN {
  vmin  =     0
  vmax  =  1000
  vint  =   100
  big   =  9000
  vmiss = -9000

  thresh[0] = -big
  k = 0 
  for(v = vmin; v < vmax; v += vint)
  {
    k++
    thresh[k] = v
  }
  kmax = k+1
  thresh[kmax]   = vmax
  thresh[kmax+1] = big
}

$3+0 != vmiss {
  v = $3+0
  kselect = -1
  for(k = 0; k <= kmax+1; k++)
  {
    if( (v >= thresh[k]) && (v < thresh[k+1]) ) {
      kselect = k
    }
  }
  if(kselect == -1) { print "histogram.awk: interval not found.", $1, $2, $3 }
  else              { count[kselect]++ }
}

END {
  print "#interval-No.  .GE.  .LT.  count"
  for(k = 0; k <= kmax; k++)
  {
    print k, thresh[k], thresh[k+1], count[k]+0
  }
}
