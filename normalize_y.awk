{
  x[NR]=$1;
  y[NR]=$2;

  ytot+=$2;
}
END{
  for(i in x) {
    print x[i], y[i]/ytot;
  }
}
