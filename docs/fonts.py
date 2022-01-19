# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [raw] raw_mimetype="text/restructuredtext"
# .. _ug_fonts:
#
#
# Font selection
# ==============
#
# Proplot registers several new fonts and includes tools
# for adding your own fonts. These features are described below.
#
#
# %% [raw] raw_mimetype="text/restructuredtext"
# .. _ug_fonts_included:
#
# Included fonts
# --------------
#
# Matplotlib provides a `~matplotlib.font_manager` module for working with
# system fonts and classifies fonts into `five font families
# <https://matplotlib.org/stable/gallery/text_labels_and_annotations/fonts_demo.html>`__:
# :rcraw:`font.serif` :rcraw:`font.sans-serif`, :rcraw:`font.monospace`,
# :rcraw:`font.cursive`, and :rcraw:`font.fantasy`. The default font family
# is sans-serif, because sans-serif fonts are generally more suitable for
# figures than serif fonts, and the default font name belonging to this family
# is `DejaVu Sans <https://dejavu-fonts.github.io>`__, which comes packaged with
# matplotlib.
#
# Matplotlib uses DejaVu Sans in part because it includes glyphs for a very wide
# range of symbols, especially mathematical symbols. However in our opinion,
# DejaVu Sans is not very aesthetically pleasing. To improve the font selection while
# keeping things consistent across different workstations, proplot is packaged
# the open source `TeX Gyre fonts <https://ctan.org/pkg/tex-gyre?lang=en>`__ and a few
# additional open source sans-serif fonts. Proplot also uses the TeX Gyre fonts as the
# first (i.e., default) entries for each of matplotlib's `font family lists
# <https://matplotlib.org/stable/tutorials/text/text_props.html#default-font>`__`:
#
# * The `Century <https://en.wikipedia.org/wiki/Century_type_family>`__ lookalike
#   :rcraw:`font.serif` = ``'TeX Gyre Schola'``.
# * The `Helvetica <https://en.wikipedia.org/wiki/Helvetica>`__ lookalike
#   :rcraw:`font.sans-serif` = ``'TeX Gyre Heros'``.
# * The `Courier <https://en.wikipedia.org/wiki/Courier_(typeface)>`__ lookalike
#   :rcraw:`font.monospace` = ``'TeX Gyre Cursor'``.
# * The `Chancery <https://en.wikipedia.org/wiki/ITC_Zapf_Chancery>`__ lookalike
#   :rcraw:`font.cursive` = ``'TeX Gyre Chorus'``.
# * The `Avant Garde <https://en.wikipedia.org/wiki/ITC_Avant_Garde>`__ lookalike
#   :rcraw:`font.fantasy` = ``'TeX Gyre Adventor'``.
#
# After importing proplot, the default matplotlib font will be
# `TeX Gyre Heros <https://ctan.org/pkg/tex-gyre-heros>`__,
# which emulates the more conventional and (in our opinion) aesthetically pleasing
# font `Helvetica <https://en.wikipedia.org/wiki/Helvetica>`__. The new default font
# family lists are shown in the :ref:`default proplotrc file <ug_proplotrc>`.
#
# To compare different fonts, use the `~proplot.demos.show_fonts` command with the
# `family` keyword (default behavior is ``family='sans-serif'``). Tables of the TeX
# Gyre and sans-serif fonts packaged with proplot are shown below. In order to show how
# the fonts perform as math text, the demo is rendered with :rcraw:`mathtext.default`
# = ``'regular'``, :rcraw:`mathtext.fontset` = ``'custom'``, and
# :rcraw:`mathtext.fallback` = ``None``. This uses the global :rcraw:`font.family`
# for the math text and shows a dummy glyph "¤" is shown where math characters
# are unavailable (see the matplotlib `math text guide
# <https://matplotlib.org/stable/tutorials/text/mathtext.html#custom-fonts>`__
# for details). In practice, proplot uses a standard non-italicized math
# text everywhere by setting :rc:`mathtext.fontset` = ``'stixsans'`` and
# :rcraw:`mathtext.default = 'rm'` (see the :ref:`proplotrc file <ug_proplotrc>`
# for details).

# %%
import proplot as pplt
fig, axs = pplt.show_fonts(family='tex-gyre')

# %%
import proplot as pplt
fig, axs = pplt.show_fonts(family='sans-serif')

# %% [raw] raw_mimetype="text/restructuredtext"
# .. _ug_fonts_user:
#
# Using your own fonts
# --------------------
#
# You can register your own fonts by adding files to the ``fonts`` subfolder
# inside `~proplot.config.Configurator.user_folder` and calling
# `~proplot.config.register_fonts`. This command is called on import. You can
# also manually pass file paths to `~proplot.config.register_fonts`.
# To change the default font, use the `~proplot.config.rc`
# object or modify your ``proplotrc``. See the
# :ref:`configuration section <ug_config>` for details.
#
# Sometimes the font you would like to use *is* installed, but the font file
# is not stored under the matplotlib-compatible ``.ttf``, ``.otf``, or ``.afm``
# formats. For example, several macOS fonts are unavailable because they are
# stored as ``.dfont`` collections. Also, while matplotlib nominally supports
# ``.ttc`` collections, proplot ignores them because figures with ``.ttc`` fonts
# `cannot be saved as PDFs <https://github.com/matplotlib/matplotlib/issues/3135>`__.
# You can get matplotlib to use ``.dfont`` and ``.ttc`` collections by
# expanding them into individual ``.ttf`` files with the
# `DFontSplitter application <https://peter.upfold.org.uk/projects/dfontsplitter>`__,
# then saving the files in-place or in the ``~/.proplot/fonts`` folder.
#
# To find font collections, check the paths listed in ``OSXFontDirectories``,
# ``X11FontDirectories``, ``MSUserFontDirectories``, and ``MSFontDirectories``
# under the `matplotlib.font_manager` module.
