#!/usr/bin/perl

use strict;
use warnings;

my $s;

sub path {
	my $l = shift; # length remaining
	my $i = shift; # current x
	my $j = shift; # current y
	my $p = shift; # path ->[x,y]
	my $m = shift;

	if ( $i < 1 || $j < 1 || $i > $s || $j > $s ) {
		return;
	}

	if ( $m->[$i][$j] ) {
		return;
	}

	$m->[$i][$j] = $l;

	$p .= '->' if $p;
	$p .= "[$i,$j]";

	if ( $l == 1 ) {
		print $p . "\n";
	} else {
		path($l - 1, $i - 1, $j - 1, $p, $m);
		path($l - 1, $i - 1, $j + 0, $p, $m);
		path($l - 1, $i - 1, $j + 1, $p, $m);
		path($l - 1, $i + 0, $j - 1, $p, $m);
		path($l - 1, $i + 0, $j + 1, $p, $m);
		path($l - 1, $i + 1, $j - 1, $p, $m);
		path($l - 1, $i + 1, $j + 0, $p, $m);
		path($l - 1, $i + 1, $j + 1, $p, $m);
	}

	$m->[$i][$j] = 0;
}

sub main {
	$s = shift // die "Must give table size!";

	for ( my $i = 1 ; $i <= $s ; $i++ ) {
		for ( my $j = 1 ; $j <= $s ; $j++ ) {
			path($s * $s, $i, $j, '');
		}
	}

	return 0;
}

exit main(@ARGV);
