# shell.nix
{ pkgs ? import <nixpkgs> {} }:
let
  python-with-my-packages = pkgs.python3.withPackages (p: with p; [
    requests
    # other python packages you want
  ]);
in
python-with-my-packages.env # replacement for pkgs.mkShell
