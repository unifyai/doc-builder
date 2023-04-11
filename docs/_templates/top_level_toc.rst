{{name | underline}}

.. This is a placeholder so the include directive removes what's before it
.. REMOVE_BEFORE_HERE
.. autosummary::
   :toctree: {% block name %}{{name}}{% endblock %}
   :template: {% block template %}top_level_module.rst{% endblock %}
   :caption: {{fullname}}
   

   :recursive:
{% for submodule in modules %}
   {{ submodule }}
{%- endfor %}
