{% extends "top_level_module.rst" %}

{% block custom_content %}
{% if modules|length != 0 %}
.. autosummary::
  :toctree: {{fullname}}
  :template: top_level_module.rst
  :recursive:
  
{% for submodule in modules %}  {{submodule}}
{% endfor %}
{% endif -%}
{% endblock %}


{# replace template with last_level_toc.rst to generate autosummary for sub module and then automodule #}
{# replace template with top_level_module.rst to generate automodule for sub module #}