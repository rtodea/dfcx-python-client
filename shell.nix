# shell.nix
{ pkgs ? import <nixpkgs> {
    config.allowUnfree = true;  # This allows unfree software
  } 
}:

pkgs.mkShell {
  buildInputs = [ 
    pkgs.python312Full 
    pkgs.jetbrains.pycharm-professional 
    pkgs.stdenv.cc.cc 
  ];
  shellHook = ''
    export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib"
  '';
}
