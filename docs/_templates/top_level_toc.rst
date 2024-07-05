{% block name %}{% endblock %}

.. autosummary::{% block options %}
    :toctree: {{name}}
    :template: {% block template %}top_level_module.rst{% endblock %}
    :recursive:
{% endblock %}
{% for submodule in modules %}
    {{ submodule }}
{%- endfor %}

{% block custom_content %}{% endblock %}
