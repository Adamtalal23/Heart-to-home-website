# Heart To Home website

*From our heart to your home.*

- `site/` is the live website Netlify publishes (see `netlify.toml`).
- `build/build.py` regenerates every page in `site/` from one file. Edit text there, then run `python3 build/build.py`.
- Photos live in `site/images/`; the gallery list is `PHOTOS` at the top of `site/site.js`.
- `build/photos.py` and `build/kitchenmask.py` are the scripts used to resize and blur photos and to build the color-tool wall mask.
- Estimate requests come in through Netlify Forms (form name `estimate`).
