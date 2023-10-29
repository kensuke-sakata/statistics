BEGIN {
  if( cutoff == "" ) {
    cutoff = 100;
    print "info: using default cutoff = 100; override using -v cutoff=x" \
      >"/dev/stderr";
  }
  v_crit = cutoff;
  n_crit = 0;
}

{
  v = $1;
  while( v > v_crit ) {
    if( n_crit > 0 ) {
      print v_crit, n_crit;
    }
    v_crit += cutoff;
    n_crit  = 0;
  }
  n_crit++;
}
END{
  if( n_crit > 0 ) {
    print v_crit, n_crit;
  }
}
