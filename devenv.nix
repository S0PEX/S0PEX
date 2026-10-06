{ pkgs, ... }:
{
  packages = [ pkgs.git ];

  languages.python = {
    enable = true;
    venv.enable = true;
    venv.requirements = ./scripts/requirements-portrait.txt;
  };

  git-hooks.hooks = {
    ruff.enable = true;
    ruff-format.enable = true;
    prettier = {
      enable = true;
      excludes = [ "^data/" "^img/" ];
    };
    check-yaml.enable = true;
    end-of-file-fixer = {
      enable = true;
      excludes = [ "^data/" "^img/" "^devenv.lock$" ];
    };
    trim-trailing-whitespace = {
      enable = true;
      excludes = [ "^data/" "^img/" "^devenv.lock$" ];
    };
  };
}
