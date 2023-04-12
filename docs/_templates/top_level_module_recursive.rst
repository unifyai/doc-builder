{% extends "top_level_module.rst" %}

{% block toctree %}
{% if modules|length != 0 %}
.. autosummary::
  :toctree: {{fullname}}
  :template: top_level_module.rst
  :recursive:
  
{% for submodule in modules %}  {{submodule}}
{% endfor %}
{% endif -%}
{% endblock %}
