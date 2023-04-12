{% block name %}{{name | escape | underline}}{% endblock %}

.. This is a placeholder so the include directive removes what's before it
.. Will set here for backwards compatibility TODO remove it
.. REMOVE_BEFORE_HERE
.. autosummary::{% block options %}
    :toctree: {{name}}
    :template: {% block template %}top_level_module.rst{% endblock %}
    :recursive:
{% endblock %}
{% for submodule in modules %}
    {{ submodule }}
{%- endfor %}

{% block custom_content %}{% endblock %}
