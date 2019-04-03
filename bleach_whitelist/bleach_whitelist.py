all_tags = [
    "a", "abbr", "acronym", "address", "applet", "area", "article", "aside", "audio",
    "b", "base", "basefont", "bdi", "bdo", "bgsound", "big", "blink", "blockquote", "body", "br", "button",
    "canvas", "caption", "center", "cite", "code", "col", "colgroup", "command", "content",
    "data", "datalist", "dd", "del", "detals", "dfn", "dialog", "dir", "div", "dl", "dt",
    "element", "em", "embed",
    "fieldset", "figcaption", "figure", "font", "footer", "form", "frame", "frameset",
    "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html",
    "i", "iframe", "image", "img", "input", "ins", "isindex",
    "kbd", "keygen",
    "label", "legend", "li", "link", "listing",
    "main", "map", "mark", "marquee", "menu", "menuitem", "meta", "meter", "multicol",
    "nav", "nobr", "noembed", "noframes", "noscript",
    "object", "ol", "optgroup", "option", "output",
    "p", "param", "picture", "plaintext", "pre", "progress",
    "q",
    "rp", "rt", "ruby",
    "s", "samp", "script", "section", "select", "shadow", "small", "source", "spacer", "span", "strike", "strong", "style", "sub", "summary", "sup",
    "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "tt",
    "u", "ul",
    "var", "video",
    "wbr",
    "xmp",
]

# List tags that, if included in a page, could break markup or open XSS.
generally_xss_unsafe = [
    "applet", "audio",
    "bgsound", "body",
    "canvas",
    "embed",
    "frame", "frameset",
    "head", "html",
    "iframe",
    "link",
    "meta",
    "object",
    "param",
    "source", "script",
    "ruby", "rt",
    "title", "track",
    "video",
    "xmp"
]

# Tags that, if included on the page, will probably not break markup or open
# XSS.  Note that these must be combined with attribute whitelisting, or things
# like <img> and <style> could still be unsafe.
generally_xss_safe = list(set(all_tags) - set(generally_xss_unsafe))
generally_xss_safe.sort()

# Tags suitable for rendering markdown
markdown_tags = [
    "h1", "h2", "h3", "h4", "h5", "h6",
    "b", "i", "strong", "em", "tt",
    "p", "br",
    "span", "div", "blockquote", "code", "hr",
    "ul", "ol", "li", "dd", "dt",
    "img",
    "a",
    "sub", "sup",
]

markdown_attrs = {
    "img": ["src", "alt", "title"],
    "a": ["href", "alt", "title"],
}

# Tags suitable for preparing documents for printing.
print_tags = [
    "h1", "h2", "h3", "h4", "h5", "h6",
    "b", "i", "strong", "em", "tt",
    "p", "br",
    "span", "div", "blockquote", "code", "hr",
    "ul", "ol", "li", "dd", "dt",
    "table", "thead", "tbody", "tfoot", "tr", "th", "td",
    "img",
]
print_attrs = {
    "*": ["class", "style"],
    "img": ["src", "width", "height"],
}

standard_styles = [
    # Taken from https://developer.mozilla.org/en-US/docs/Web/CSS/Reference
    # This includes pseudo-classes, pseudo-elements, @-rules, units, and
    # selectors in addition to properties, but it doesn't matter for our
    # purposes -- we don't need to filter styles..
    ":active", "::after (:after)", "align-content", "align-items", "align-self",
    "all", "<angle>", "animation", "animation-delay", "animation-direction",
    "animation-duration", "animation-fill-mode", "animation-iteration-count",
    "animation-name", "animation-play-state", "animation-timing-function",
    "@annotation", "annotation()", "attr()", "::backdrop", "backface-visibility",
    "background", "background-attachment", "background-blend-mode",
    "background-clip", "background-color", "background-image", "background-origin",
    "background-position", "background-repeat", "background-size", "<basic-shape>",
    "::before (:before)", "<blend-mode>", "blur()", "border", "border-bottom",
    "border-bottom-color", "border-bottom-left-radius",
    "border-bottom-right-radius", "border-bottom-style", "border-bottom-width",
    "border-collapse", "border-color", "border-image", "border-image-outset",
    "border-image-repeat", "border-image-slice", "border-image-source",
    "border-image-width", "border-left", "border-left-color", "border-left-style",
    "border-left-width", "border-radius", "border-right", "border-right-color",
    "border-right-style", "border-right-width", "border-spacing", "border-style",
    "border-top", "border-top-color", "border-top-left-radius",
    "border-top-right-radius", "border-top-style", "border-top-width",
    "border-width", "bottom", "box-decoration-break", "box-shadow", "box-sizing",
    "break-after", "break-before", "break-inside", "brightness()", "calc()",
    "caption-side", "ch", "@character-variant", "character-variant()", "@charset",
    ":checked", "circle()", "clear", "clip", "clip-path", "cm", "color", "<color>",
    "columns", "column-count", "column-fill", "column-gap", "column-rule",
    "column-rule-color", "column-rule-style", "column-rule-width", "column-span",
    "column-width", "content", "contrast()", "<counter>", "counter-increment",
    "counter-reset", "@counter-style", "cubic-bezier()", "cursor",
    "<custom-ident>", ":default", "deg", ":dir()", "direction", ":disabled",
    "display", "@document", "dpcm", "dpi", "dppx", "drop-shadow()", "element()",
    "ellipse()", "em", ":empty", "empty-cells", ":enabled", "ex", "filter",
    ":first", ":first-child", "::first-letter", "::first-line",
    ":first-of-type", "flex", "flex-basis", "flex-direction",
    "flex-flow", "flex-grow", "flex-shrink", "flex-wrap", "float", ":focus",
    "font", "@font-face", "font-family", "font-feature-settings",
    "@font-feature-values", "font-kerning", "font-language-override", "font-size",
    "font-size-adjust", "font-stretch", "font-style", "font-synthesis",
    "font-variant", "font-variant-alternates", "font-variant-caps",
    "font-variant-east-asian", "font-variant-ligatures", "font-variant-numeric",
    "font-variant-position", "font-weight", "<frequency>", ":fullscreen", "grad",
    "<gradient>", "grayscale()", "grid", "grid-area", "grid-auto-columns",
    "grid-auto-flow", "grid-auto-position", "grid-auto-rows", "grid-column",
    "grid-column-start", "grid-column-end", "grid-row", "grid-row-start",
    "grid-row-end", "grid-template", "grid-template-areas", "grid-template-rows",
    "grid-template-columns", "height", ":hover", "hsl()", "hsla()", "hue-rotate()",
    "hyphens", "hz", "<image>", "image()", "image-rendering", "image-resolution",
    "image-orientation", "ime-mode", "@import", "in", ":indeterminate", "inherit",
    "initial", ":in-range", "inset()", "<integer>", ":invalid", "invert()",
    "isolation", "justify-content", "@keyframes", "khz", ":lang()", ":last-child",
    ":last-of-type", "left", ":left", "<length>", "letter-spacing",
    "linear-gradient()", "line-break", "line-height", ":link", "list-style",
    "list-style-image", "list-style-position", "list-style-type", "margin",
    "margin-bottom", "margin-left", "margin-right", "margin-top", "marks", "mask",
    "mask-type", "matrix()", "matrix3d()", "max-height", "max-width", "@media",
    "min-height", "minmax()", "min-width", "mix-blend-mode", "mm", "ms",
    "@namespace", ":not()", ":nth-child()", ":nth-last-child()",
    ":nth-last-of-type()", ":nth-of-type()", "<number>", "object-fit",
    "object-position", ":only-child", ":only-of-type", "opacity", "opacity()",
    ":optional", "order", "@ornaments", "ornaments()", "orphans", "outline",
    "outline-color", "outline-offset", "outline-style", "outline-width",
    ":out-of-range", "overflow", "overflow-wrap", "overflow-x", "overflow-y",
    "padding", "padding-bottom", "padding-left", "padding-right", "padding-top",
    "@page", "page-break-after", "page-break-before", "page-break-inside", "pc",
    "<percentage>", "perspective", "perspective()", "perspective-origin",
    "pointer-events", "polygon()", "position", "<position>", "pt", "px", "quotes",
    "rad", "radial-gradient()", "<ratio>", ":read-only", ":read-write", "rect()",
    "rem", "repeat()", "::repeat-index", "::repeat-item",
    "repeating-linear-gradient()", "repeating-radial-gradient()", ":required",
    "resize", "<resolution>", "rgb()", "rgba()", "right", ":right", ":root",
    "rotate()", "rotatex()", "rotatey()", "rotatez()", "rotate3d()", "ruby-align",
    "ruby-merge", "ruby-position", "s", "saturate()", "scale()", "scalex()",
    "scaley()", "scalez()", "scale3d()", ":scope", "scroll-behavior",
    "::selection", "sepia()", "<shape>", "shape-image-threshold", "shape-margin",
    "shape-outside", "skew()", "skewx()", "skewy()", "steps()", "<string>",
    "@styleset", "styleset()", "@stylistic", "stylistic()", "@supports", "@swash",
    "swash()", "symbol()", "table-layout", "tab-size", ":target", "text-align",
    "text-align-last", "text-combine-upright", "text-decoration",
    "text-decoration-color", "text-decoration-line", "text-decoration-style",
    "text-indent", "text-orientation", "text-overflow", "text-rendering",
    "text-shadow", "text-transform", "text-underline-position", "<time>",
    "<timing-function>", "top", "touch-action", "transform", "transform-origin",
    "transform-style", "transition", "transition-delay", "transition-duration",
    "transition-property", "transition-timing-function", "translate()",
    "translatex()", "translatey()", "translatez()", "translate3d()", "turn",
    "unicode-bidi", "unicode-range", "unset", "<uri>", "url()", "<user-ident>",
    ":valid", "::value", "var()", "vertical-align", "vh", "@viewport",
    "visibility", ":visited", "vmax", "vmin", "vw", "white-space", "widows",
    "width", "will-change", "word-break", "word-spacing", "word-wrap",
    "writing-mode", "z-index",

]

webkit_prefixed_styles = [
    # Webkit-prefixed styles
    # https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Webkit_Extensions
    "-webkit-animation", "-webkit-animation-delay", "-webkit-animation-direction",
    "-webkit-animation-duration", "-webkit-animation-fill-mode",
    "-webkit-animation-iteration-count", "-webkit-animation-name",
    "-webkit-animation-play-state", "-webkit-animation-timing-function",
    "-webkit-backface-visibility", "-webkit-border-image", "-webkit-column-count",
    "-webkit-column-gap", "-webkit-column-width", "-webkit-column-rule",
    "-webkit-column-rule-width", "-webkit-column-rule-style",
    "-webkit-column-rule-color", "-webkit-columns", "-webkit-column-span",
    "-webkit-font-feature-settings", "-webkit-font-kerning",
    "-webkit-font-size-delta", "-webkit-font-variant-ligatures",
    "-webkit-grid-column", "-webkit-grid-row", "-webkit-hyphens", "-webkit-mask",
    "-webkit-mask-clip", "-webkit-mask-composite", "-webkit-mask-image",
    "-webkit-mask-origin", "-webkit-mask-position", "-webkit-mask-repeat",
    "-webkit-mask-size", "-webkit-perspective", "-webkit-perspective-origin",
    "-webkit-region-fragment", "-webkit-shape-outside", "-webkit-text-emphasis",
    "-webkit-text-emphasis-color", "-webkit-text-emphasis-position",
    "-webkit-text-emphasis-style", "-webkit-transform", "-webkit-transform-origin",
    "-webkit-transform-style", "-webkit-transition", "-webkit-transition-delay",
    "-webkit-transition-duration", "-webkit-transition-property",
    "-webkit-transition-timing-function", "-epub-word-break", "-epub-writing-mode",
    # WebKit-prefixed properties with an unprefixed counterpart
    "-webkit-background-clip", "-webkit-background-origin",
    "-webkit-background-size", "-webkit-border-bottom-left-radius",
    "-webkit-border-bottom-right-radius", "-webkit-border-radius",
    "-webkit-border-top-left-radius", "-webkit-border-top-right-radius",
    "-webkit-box-sizing", "-epub-caption-side", "-webkit-opacity",
    "-epub-text-transform",
]

mozilla_prefixed_styles = [
    "-moz-column-count", "-moz-column-fill", "-moz-column-gap",
    "-moz-column-width", "-moz-column-rule", "-moz-column-rule-width",
    "-moz-column-rule-style", "-moz-column-rule-color",
    "-moz-font-feature-settings", "-moz-font-language-override", "-moz-hyphens",
    "-moz-text-align-last", "-moz-text-decoration-color",
    "-moz-text-decoration-line", "-moz-text-decoration-style",
]

all_prefixed_styles = [
    # From http://peter.sh/experiments/vendor-prefixed-css-property-overview/
    "-ms-accelerator", "-webkit-app-region", "-webkit-appearance",
    "-webkit-appearance", "-moz-appearance", "-webkit-aspect-ratio",
    "-webkit-backdrop-filter", "backface-visibility",
    "-webkit-backface-visibility", "backface-visibility", "backface-visibility",
    "-webkit-background-composite", "-webkit-background-composite", "-moz-binding",
    "-ms-block-progression", "-webkit-border-after", "-webkit-border-after",
    "-webkit-border-after-color", "-webkit-border-after-color",
    "-webkit-border-after-style", "-webkit-border-after-style",
    "-webkit-border-after-width", "-webkit-border-after-width",
    "-webkit-border-before", "-webkit-border-before",
    "-webkit-border-before-color", "-webkit-border-before-color",
    "-webkit-border-before-style", "-webkit-border-before-style",
    "-webkit-border-before-width", "-webkit-border-before-width",
    "-moz-border-bottom-colors", "-webkit-border-end", "-webkit-border-end",
    "-moz-border-end", "-webkit-border-end-color", "-webkit-border-end-color",
    "-moz-border-end-color", "-webkit-border-end-style",
    "-webkit-border-end-style", "-moz-border-end-style",
    "-webkit-border-end-width", "-webkit-border-end-width",
    "-moz-border-end-width", "-webkit-border-fit",
    "-webkit-border-horizontal-spacing", "-webkit-border-horizontal-spacing",
    "-moz-border-left-colors", "-moz-border-right-colors", "-webkit-border-start",
    "-webkit-border-start", "-moz-border-start", "-webkit-border-start-color",
    "-webkit-border-start-color", "-moz-border-start-color",
    "-webkit-border-start-style", "-webkit-border-start-style",
    "-moz-border-start-style", "-webkit-border-start-width",
    "-webkit-border-start-width", "-moz-border-start-width",
    "-moz-border-top-colors", "-webkit-border-vertical-spacing",
    "-webkit-border-vertical-spacing", "-webkit-box-align", "-webkit-box-align",
    "-moz-box-align", "-webkit-box-decoration-break",
    "-webkit-box-decoration-break", "box-decoration-break",
    "-webkit-box-direction", "-webkit-box-direction", "-moz-box-direction",
    "-webkit-box-flex", "-webkit-box-flex", "-moz-box-flex",
    "-webkit-box-flex-group", "-webkit-box-flex-group", "-webkit-box-lines",
    "-webkit-box-lines", "-webkit-box-ordinal-group", "-webkit-box-ordinal-group",
    "-moz-box-ordinal-group", "-webkit-box-orient", "-webkit-box-orient",
    "-moz-box-orient", "-webkit-box-pack", "-webkit-box-pack", "-moz-box-pack",
    "-webkit-box-reflect", "-webkit-box-reflect", "clip-path", "-webkit-clip-path",
    "clip-path", "clip-path", "-webkit-color-correction", "-webkit-column-axis",
    "-webkit-column-break-after", "-webkit-column-break-after",
    "-webkit-column-break-before", "-webkit-column-break-before",
    "-webkit-column-break-inside", "-webkit-column-break-inside",
    "-webkit-column-count", "column-count", "-moz-column-count", "column-count",
    "column-fill", "column-fill", "-moz-column-fill", "column-fill",
    "-webkit-column-gap", "column-gap", "-moz-column-gap", "column-gap",
    "-webkit-column-rule", "column-rule", "-moz-column-rule", "column-rule",
    "-webkit-column-rule-color", "column-rule-color", "-moz-column-rule-color",
    "column-rule-color", "-webkit-column-rule-style", "column-rule-style",
    "-moz-column-rule-style", "column-rule-style", "-webkit-column-rule-width",
    "column-rule-width", "-moz-column-rule-width", "column-rule-width",
    "-webkit-column-span", "column-span", "column-span", "-webkit-column-width",
    "column-width", "-moz-column-width", "column-width", "-webkit-columns",
    "columns", "-moz-columns", "columns", "-ms-content-zoom-chaining",
    "-ms-content-zoom-limit", "-ms-content-zoom-limit-max",
    "-ms-content-zoom-limit-min", "-ms-content-zoom-snap",
    "-ms-content-zoom-snap-points", "-ms-content-zoom-snap-type",
    "-ms-content-zooming", "-moz-control-character-visibility",
    "-webkit-cursor-visibility", "-webkit-dashboard-region", "filter",
    "-webkit-filter", "filter", "filter", "-ms-flex-align", "-ms-flex-item-align",
    "-ms-flex-line-pack", "-ms-flex-negative", "-ms-flex-order", "-ms-flex-pack",
    "-ms-flex-positive", "-ms-flex-preferred-size", "-moz-float-edge",
    "-webkit-flow-from", "-ms-flow-from", "-webkit-flow-into", "-ms-flow-into",
    "-webkit-font-feature-settings", "-webkit-font-feature-settings",
    "font-feature-settings", "font-feature-settings", "font-kerning",
    "-webkit-font-kerning", "font-kerning", "-webkit-font-size-delta",
    "-webkit-font-size-delta", "-webkit-font-smoothing", "-webkit-font-smoothing",
    "font-variant-ligatures", "-webkit-font-variant-ligatures",
    "font-variant-ligatures", "-moz-force-broken-image-icon", "grid",
    "-webkit-grid", "grid", "grid-area", "-webkit-grid-area", "grid-area",
    "grid-auto-columns", "-webkit-grid-auto-columns", "grid-auto-columns",
    "grid-auto-flow", "-webkit-grid-auto-flow", "grid-auto-flow", "grid-auto-rows",
    "-webkit-grid-auto-rows", "grid-auto-rows", "grid-column",
    "-webkit-grid-column", "grid-column", "-ms-grid-column",
    "-ms-grid-column-align", "grid-column-end", "-webkit-grid-column-end",
    "grid-column-end", "-ms-grid-column-span", "grid-column-start",
    "-webkit-grid-column-start", "grid-column-start", "-ms-grid-columns",
    "grid-row", "-webkit-grid-row", "grid-row", "-ms-grid-row",
    "-ms-grid-row-align", "grid-row-end", "-webkit-grid-row-end", "grid-row-end",
    "-ms-grid-row-span", "grid-row-start", "-webkit-grid-row-start",
    "grid-row-start", "-ms-grid-rows", "grid-template", "-webkit-grid-template",
    "grid-template", "grid-template-areas", "-webkit-grid-template-areas",
    "grid-template-areas", "grid-template-columns",
    "-webkit-grid-template-columns", "grid-template-columns", "grid-template-rows",
    "-webkit-grid-template-rows", "grid-template-rows", "-ms-high-contrast-adjust",
    "-webkit-highlight", "-webkit-hyphenate-character",
    "-webkit-hyphenate-character", "-webkit-hyphenate-limit-after",
    "-webkit-hyphenate-limit-before", "-ms-hyphenate-limit-chars",
    "-webkit-hyphenate-limit-lines", "-ms-hyphenate-limit-lines",
    "-ms-hyphenate-limit-zone", "-webkit-hyphens", "-moz-hyphens", "-ms-hyphens",
    "-moz-image-region", "-ms-ime-align", "-webkit-initial-letter",
    "-ms-interpolation-mode", "justify-self", "-webkit-justify-self",
    "-webkit-line-align", "-webkit-line-box-contain", "-webkit-line-box-contain",
    "-webkit-line-break", "-webkit-line-break", "line-break", "-webkit-line-clamp",
    "-webkit-line-clamp", "-webkit-line-grid", "-webkit-line-snap",
    "-webkit-locale", "-webkit-locale", "-webkit-logical-height",
    "-webkit-logical-height", "-webkit-logical-width", "-webkit-logical-width",
    "-webkit-margin-after", "-webkit-margin-after",
    "-webkit-margin-after-collapse", "-webkit-margin-after-collapse",
    "-webkit-margin-before", "-webkit-margin-before",
    "-webkit-margin-before-collapse", "-webkit-margin-before-collapse",
    "-webkit-margin-bottom-collapse", "-webkit-margin-bottom-collapse",
    "-webkit-margin-collapse", "-webkit-margin-collapse", "-webkit-margin-end",
    "-webkit-margin-end", "-moz-margin-end", "-webkit-margin-start",
    "-webkit-margin-start", "-moz-margin-start", "-webkit-margin-top-collapse",
    "-webkit-margin-top-collapse", "-webkit-marquee", "-webkit-marquee-direction",
    "-webkit-marquee-increment", "-webkit-marquee-repetition",
    "-webkit-marquee-speed", "-webkit-marquee-style", "mask", "-webkit-mask",
    "mask", "-webkit-mask-box-image", "-webkit-mask-box-image",
    "-webkit-mask-box-image-outset", "-webkit-mask-box-image-outset",
    "-webkit-mask-box-image-repeat", "-webkit-mask-box-image-repeat",
    "-webkit-mask-box-image-slice", "-webkit-mask-box-image-slice",
    "-webkit-mask-box-image-source", "-webkit-mask-box-image-source",
    "-webkit-mask-box-image-width", "-webkit-mask-box-image-width",
    "-webkit-mask-clip", "-webkit-mask-clip", "-webkit-mask-composite",
    "-webkit-mask-composite", "-webkit-mask-image", "-webkit-mask-image",
    "-webkit-mask-origin", "-webkit-mask-origin", "-webkit-mask-position",
    "-webkit-mask-position", "-webkit-mask-position-x", "-webkit-mask-position-x",
    "-webkit-mask-position-y", "-webkit-mask-position-y", "-webkit-mask-repeat",
    "-webkit-mask-repeat", "-webkit-mask-repeat-x", "-webkit-mask-repeat-x",
    "-webkit-mask-repeat-y", "-webkit-mask-repeat-y", "-webkit-mask-size",
    "-webkit-mask-size", "mask-source-type", "-webkit-mask-source-type",
    "-moz-math-display", "-moz-math-variant", "-webkit-max-logical-height",
    "-webkit-max-logical-height", "-webkit-max-logical-width",
    "-webkit-max-logical-width", "-webkit-min-logical-height",
    "-webkit-min-logical-height", "-webkit-min-logical-width",
    "-webkit-min-logical-width", "-webkit-nbsp-mode", "-moz-orient",
    "-moz-osx-font-smoothing", "-moz-outline-radius",
    "-moz-outline-radius-bottomleft", "-moz-outline-radius-bottomright",
    "-moz-outline-radius-topleft", "-moz-outline-radius-topright",
    "-webkit-overflow-scrolling", "-ms-overflow-style", "-webkit-padding-after",
    "-webkit-padding-after", "-webkit-padding-before", "-webkit-padding-before",
    "-webkit-padding-end", "-webkit-padding-end", "-moz-padding-end",
    "-webkit-padding-start", "-webkit-padding-start", "-moz-padding-start",
    "perspective", "-webkit-perspective", "perspective", "perspective",
    "perspective-origin", "-webkit-perspective-origin", "perspective-origin",
    "perspective-origin", "-webkit-perspective-origin-x",
    "-webkit-perspective-origin-x", "perspective-origin-x",
    "-webkit-perspective-origin-y", "-webkit-perspective-origin-y",
    "perspective-origin-y", "-webkit-print-color-adjust",
    "-webkit-print-color-adjust", "-webkit-region-break-after",
    "-webkit-region-break-before", "-webkit-region-break-inside",
    "-webkit-region-fragment", "-webkit-rtl-ordering", "-webkit-rtl-ordering",
    "-webkit-ruby-position", "-webkit-ruby-position", "ruby-position",
    "-moz-script-level", "-moz-script-min-size", "-moz-script-size-multiplier",
    "-ms-scroll-chaining", "-ms-scroll-limit", "-ms-scroll-limit-x-max",
    "-ms-scroll-limit-x-min", "-ms-scroll-limit-y-max", "-ms-scroll-limit-y-min",
    "-ms-scroll-rails", "-webkit-scroll-snap-coordinate",
    "-webkit-scroll-snap-destination", "-webkit-scroll-snap-points-x",
    "-ms-scroll-snap-points-x", "-webkit-scroll-snap-points-y",
    "-ms-scroll-snap-points-y", "-webkit-scroll-snap-type", "-ms-scroll-snap-type",
    "-ms-scroll-snap-x", "-ms-scroll-snap-y", "-ms-scroll-translation",
    "-ms-scrollbar-3dlight-color", "shape-image-threshold",
    "-webkit-shape-image-threshold", "shape-margin", "-webkit-shape-margin",
    "shape-outside", "-webkit-shape-outside", "-moz-stack-sizing", "tab-size",
    "tab-size", "-moz-tab-size", "-webkit-tap-highlight-color",
    "-webkit-tap-highlight-color", "text-align-last", "-webkit-text-align-last",
    "-moz-text-align-last", "text-align-last", "-webkit-text-combine",
    "-webkit-text-combine", "-ms-text-combine-horizontal", "text-decoration-color",
    "-webkit-text-decoration-color", "text-decoration-color",
    "text-decoration-color", "text-decoration-line",
    "-webkit-text-decoration-line", "text-decoration-line",
    "-webkit-text-decoration-skip", "text-decoration-style",
    "-webkit-text-decoration-style", "text-decoration-style",
    "-webkit-text-decorations-in-effect", "-webkit-text-decorations-in-effect",
    "-webkit-text-emphasis", "text-emphasis", "-webkit-text-emphasis-color",
    "text-emphasis-color", "-webkit-text-emphasis-position",
    "text-emphasis-position", "-webkit-text-emphasis-style", "text-emphasis-style",
    "-webkit-text-fill-color", "-webkit-text-fill-color", "text-justify",
    "-webkit-text-justify", "text-justify", "-webkit-text-orientation",
    "-webkit-text-orientation", "text-orientation", "-webkit-text-security",
    "-webkit-text-security", "-webkit-text-size-adjust", "-moz-text-size-adjust",
    "-ms-text-size-adjust", "-webkit-text-stroke", "-webkit-text-stroke",
    "-webkit-text-stroke-color", "-webkit-text-stroke-color",
    "-webkit-text-stroke-width", "-webkit-text-stroke-width",
    "text-underline-position", "-webkit-text-underline-position",
    "text-underline-position", "-webkit-touch-callout", "-ms-touch-select",
    "transform", "-webkit-transform", "transform", "transform", "transform-origin",
    "-webkit-transform-origin", "transform-origin", "transform-origin",
    "-webkit-transform-origin-x", "-webkit-transform-origin-x",
    "transform-origin-x", "-webkit-transform-origin-y",
    "-webkit-transform-origin-y", "transform-origin-y",
    "-webkit-transform-origin-z", "-webkit-transform-origin-z",
    "transform-origin-z", "transform-style", "-webkit-transform-style",
    "transform-style", "transform-style", "-webkit-user-drag", "-webkit-user-drag",
    "-moz-user-focus", "-moz-user-input", "-webkit-user-modify",
    "-webkit-user-modify", "-moz-user-modify", "-webkit-user-select",
    "-webkit-user-select", "-moz-user-select", "-ms-user-select",
    "-moz-window-dragging", "-moz-window-shadow", "-ms-wrap-flow",
    "-ms-wrap-margin", "-ms-wrap-through", "writing-mode", "-webkit-writing-mode",
    "writing-mode", "writing-mode",
]

all_styles = standard_styles + all_prefixed_styles
