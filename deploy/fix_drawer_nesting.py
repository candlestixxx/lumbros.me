with open('deploy/homepage.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = """        </div>
      </div>
    </div>
  </div>

    <!-- =========================================================================
       LUMBROS.ME OFFICIAL SITE MENU // POSITIONED DIRECTLY UNDER SPECTRUM DECK"""

replacement = """        </div>
          </div> <!-- Close inner vision-deck-controls -->

          <!-- Drawer Bottom Collapse Row -->
          <div class="drawer-bottom-collapse-row">
            <button type="button" class="drawer-close-inline-btn" id="drawer-close-bottom-btn" title="Collapse Sub-Menu">
              ▲ COLLAPSE DEEP SPECTRUM CONTROLS
            </button>
          </div>
        </div> <!-- Close drawer-inner-frame -->
      </div> <!-- Close spectrum-submenu-drawer -->
    </div> <!-- Close vision-deck-frame -->
  </div> <!-- Close vision-calibration-deck -->

    <!-- =========================================================================
       LUMBROS.ME OFFICIAL SITE MENU // POSITIONED DIRECTLY UNDER SPECTRUM DECK"""

if target in text:
    text = text.replace(target, replacement, 1)
    print("Successfully replaced closing tags!")
else:
    print("Target not found, checking exact whitespace...")
    idx = text.find('compact-archetype-invite-strip')
    next_nav = text.find('<nav class="main-site-command-menu"', idx)
    print(text[idx+400:next_nav+100])

with open('deploy/homepage.html', 'w', encoding='utf-8') as f:
    f.write(text)
