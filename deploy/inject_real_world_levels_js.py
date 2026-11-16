"""
Inject JavaScript engine for Interactive Real-World Tech Levels (Bank & Local Brand Grocery Store with Weekly Deals).
Strictly enforce zero raw '&&' inside script tags.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEPAGE_PATH = os.path.join(BASE_DIR, 'homepage.html')

with open(HOMEPAGE_PATH, 'r', encoding='utf-8') as f:
    home = f.read()

LEVELS_JS_ENGINE = '''
    // =========================================================================
    // INTERACTIVE REAL-WORLD TECH LEVELS ENGINE (LEVELS 01 - 04)
    // BANKING RUN & LOCAL BRAND GROCERY STORE WITH INTERACTIVE WEEKLY DEALS
    // ARCHITECTED BY LUM (LUMBROS KOURLOS) // ANCHORED AT 532nm VITALITY
    // =========================================================================
    (function initRealWorldLevelsEngine() {
      // Level Stepper Tab Switching (Levels 1 to 4)
      var levelStepBtns = document.querySelectorAll('.level-step-btn');
      var levelPanes = document.querySelectorAll('.level-content-pane');

      function switchLevel(levelNum) {
        levelStepBtns.forEach(function(b) {
          b.classList.remove('active');
          b.style.background = 'rgba(5,15,25,0.7)';
          b.style.borderColor = 'rgba(0,229,255,0.3)';
          var activeIndicator = b.querySelector('div:first-child span:last-child');
          if (activeIndicator) activeIndicator.style.color = '#8ce4a7';
        });

        levelPanes.forEach(function(p) {
          p.style.display = 'none';
        });

        var activeBtn = document.getElementById('level-step-btn-' + levelNum);
        var activePane = document.getElementById('level-pane-' + levelNum);

        if (activeBtn) {
          activeBtn.classList.add('active');
          activeBtn.style.background = 'rgba(0,255,102,0.15)';
          activeBtn.style.borderColor = '#00ff66';
          var activeIndicator = activeBtn.querySelector('div:first-child span:last-child');
          if (activeIndicator) {
            activeIndicator.style.color = '#00ff66';
            activeIndicator.innerText = 'ACTIVE';
          }
        }

        if (activePane) {
          activePane.style.display = 'block';
        }
      }

      levelStepBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
          var lvl = btn.getAttribute('data-level');
          switchLevel(lvl);
        });
      });

      // -----------------------------------------------------------------------
      // LEVEL 01: BANKING & LIQUIDITY RUN ENGINE
      // -----------------------------------------------------------------------
      var bankState = {
        checking: 1420.00,
        savings: 5800.00,
        debt: 1650.00,
        paycheckArrived: true,
        institution: 'chase'
      };

      function updateBankUI() {
        var chkEl = document.getElementById('bank-checking-val');
        var savEl = document.getElementById('bank-savings-val');
        var dbtEl = document.getElementById('bank-debt-val');
        var rnwEl = document.getElementById('bank-runway-val');

        if (chkEl) chkEl.innerText = '$' + bankState.checking.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        if (savEl) savEl.innerText = '$' + bankState.savings.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        if (dbtEl) {
          if (bankState.debt > 0) {
            dbtEl.innerText = '-$' + bankState.debt.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
            dbtEl.style.color = '#ff5555';
          } else {
            dbtEl.innerText = '$0.00 [DEBT FREE]';
            dbtEl.style.color = '#00ff66';
          }
        }

        if (rnwEl) {
          var monthlyBurn = 2000.0;
          var runwayMonths = ((bankState.checking + bankState.savings) / monthlyBurn).toFixed(1);
          rnwEl.innerText = runwayMonths + ' MONTHS';
        }
      }

      // Bank Institution Select
      var instSelect = document.getElementById('bank-institution-select');
      if (instSelect) {
        instSelect.addEventListener('change', function() {
          bankState.institution = instSelect.value;
          var feed = document.getElementById('bank-terminal-feed');
          if (feed) {
            if (bankState.institution === 'credit_union') {
              feed.innerHTML = '⟦ CREDIT UNION CORE ⟧ Switched to member-owned institution. Zero monthly maintenance fees locked. Dividend yield +0.25%.';
            } else if (bankState.institution === 'sovereign_defi') {
              feed.innerHTML = '⟦ SOVEREIGN VAULT ⟧ Direct self-custody treasury connected. Automated 4.85% APY yield daily streaming.';
            } else {
              feed.innerHTML = '⟦ TIER-1 BANK CORE ⟧ Commercial banking active. FDIC insured standard rails.';
            }
          }
        });
      }

      // Bank Action 1: Kill Credit Card Debt
      var btnKillDebt = document.getElementById('btn-bank-kill-debt');
      if (btnKillDebt) {
        btnKillDebt.addEventListener('click', function() {
          if (bankState.debt <= 0) {
            var feed = document.getElementById('bank-terminal-feed');
            if (feed) feed.innerText = '⟦ BANK TERMINAL ⟧ Credit card is already completely paid off! Zero debt.';
            return;
          }

          var payAmount = Math.min(bankState.checking + 2850, bankState.debt);
          bankState.checking = (bankState.checking + 2850) - payAmount;
          bankState.debt = 0;
          updateBankUI();

          var feed = document.getElementById('bank-terminal-feed');
          if (feed) {
            feed.innerHTML = '<span style="color:#00ff66;">✔ SUCCESS:</span> Direct deposit allocated. Paid off $' + payAmount.toFixed(2) + ' credit card balance in full! Eliminated 24.9% APR interest bleed permanently.';
          }

          // Boost Soul Calculator
          if (window.adjustSoulCalculator) {
            window.adjustSoulCalculator(8, 6, 10, 12);
          }
        });
      }

      // Bank Action 2: Balanced 50/50 Strategy
      var btnSplitStrat = document.getElementById('btn-bank-split-strategy');
      if (btnSplitStrat) {
        btnSplitStrat.addEventListener('click', function() {
          bankState.checking += 850;
          bankState.savings += 1000;
          bankState.debt = Math.max(0, bankState.debt - 1000);
          updateBankUI();

          var feed = document.getElementById('bank-terminal-feed');
          if (feed) {
            feed.innerHTML = '<span style="color:#00e5ff;">⚖️ BALANCED ALLOCATION:</span> Paid $1,000 toward debt, deposited $1,000 into High-Yield Savings, and kept $850 liquid in Checking.';
          }

          if (window.adjustSoulCalculator) {
            window.adjustSoulCalculator(5, 5, 7, 8);
          }
        });
      }

      // Bank Action 3: AI Financial Negotiator
      var btnAiDispute = document.getElementById('btn-bank-ai-dispute');
      if (btnAiDispute) {
        btnAiDispute.addEventListener('click', function() {
          var feeRefund = 35.00;
          bankState.checking += feeRefund;
          updateBankUI();

          var feed = document.getElementById('bank-terminal-feed');
          if (feed) {
            feed.innerHTML = '<span style="color:#ffaa00;">🤖 AI AGENT DEPLOYED:</span> Contacted bank customer operations. Automated dispute succeeded: $35.00 maintenance fee waived and credited back to checking!';
          }

          if (window.adjustSoulCalculator) {
            window.adjustSoulCalculator(7, 3, 6, 6);
          }
        });
      }

      // -----------------------------------------------------------------------
      // LEVEL 02: LOCAL BRAND GROCERY STORE & WEEKLY DEALS ENGINE
      // -----------------------------------------------------------------------
      var groceryCart = [];
      var currentStore = 'kroger';

      var storeCatalogInfo = {
        kroger: {
          title: 'KROGER SUPERMARKET // THIS WEEK\'S OFFICIAL DIGITAL CIRCULAR',
          subtitle: 'Clip digital coupons & fuel points for mega-savings on family pantry essentials.'
        },
        trader_joes: {
          title: 'TRADER JOE\'S // SPECIALTY ORGANIC PRODUCE & FEARLESS FLYER',
          subtitle: 'Nutrient-dense clean ingredients, sourdough bakery, and wholesale values without coupons.'
        },
        aldi: {
          title: 'ALDI // DEEP DISCOUNT ESSENTIALS & FRUGAL MASTER-PLAN',
          subtitle: 'Zero overhead private brand staples maximizing your family\'s grocery runway.'
        },
        whole_foods: {
          title: 'WHOLE FOODS MARKET // 532nm CLEAN ORGANIC GREEN NUTRITION',
          subtitle: 'Prime savings on pasture-raised meats, wild-caught fish, and pure phytonutrients.'
        },
        meijer: {
          title: 'MEIJER // MIDWEST PRIDE & BULK FAMILY VALUE',
          subtitle: 'Local community farm harvests, bulk household supplies, and mPerks digital coupons.'
        }
      };

      // Store Brand Selector
      var storeSelect = document.getElementById('grocery-brand-select');
      if (storeSelect) {
        storeSelect.addEventListener('change', function() {
          currentStore = storeSelect.value;
          var info = storeCatalogInfo[currentStore];
          var headline = document.getElementById('grocery-store-headline');
          if (headline) {
            if (info) {
              headline.innerText = info.title;
            }
          }
          var receiptFeed = document.getElementById('grocery-receipt-feed');
          if (receiptFeed) {
            receiptFeed.innerText = '⟦ STORE CHANGED ⟧ Welcome to ' + (info ? info.title : currentStore.toUpperCase()) + '. Weekly circular prices loaded.';
          }
        });
      }

      function updateGroceryCartUI() {
        var countEl = document.getElementById('cart-item-count');
        var savEl = document.getElementById('cart-savings-display');
        var totEl = document.getElementById('cart-total-display');
        var listEl = document.getElementById('cart-items-list');
        var vitEl = document.getElementById('cart-vitality-score');

        var totalSale = 0;
        var totalReg = 0;
        var vitalitySum = 0;

        for (var i = 0; i < groceryCart.length; i++) {
          totalSale += groceryCart[i].sale;
          totalReg += groceryCart[i].reg;
          vitalitySum += groceryCart[i].vit;
        }

        var totalSavings = totalReg - totalSale;
        if (totalSavings < 0) totalSavings = 0;

        if (countEl) countEl.innerText = groceryCart.length + ' Items';
        if (savEl) savEl.innerText = '-$' + totalSavings.toFixed(2);
        if (totEl) totEl.innerText = '$' + totalSale.toFixed(2);

        if (vitEl) {
          var vitScore = Math.min(100, 75 + vitalitySum);
          vitEl.innerText = vitScore + '% [532nm OPTIMAL]';
        }

        if (listEl) {
          if (groceryCart.length === 0) {
            listEl.innerHTML = '<span style="color: #64748b;">Cart is empty. Click any weekly deal button above to clip digital coupons and build your cart!</span>';
          } else {
            var itemsHtml = '';
            for (var j = 0; j < groceryCart.length; j++) {
              var it = groceryCart[j];
              itemsHtml += '<div style="display: flex; justify-content: space-between; padding: 2px 0; border-bottom: 1px dotted rgba(255,255,255,0.1);">' +
                           '<span>' + it.name + '</span>' +
                           '<span><strong style="color:#00ff66;">$' + it.sale.toFixed(2) + '</strong> <span style="text-decoration:line-through; color:#64748b; font-size:0.65rem;">$' + it.reg.toFixed(2) + '</span></span>' +
                           '</div>';
            }
            listEl.innerHTML = itemsHtml;
          }
        }
      }

      // Clip Deal Buttons
      var clipBtns = document.querySelectorAll('.btn-clip-deal');
      clipBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
          var id = btn.getAttribute('data-id');
          var name = btn.getAttribute('data-name');
          var sale = parseFloat(btn.getAttribute('data-sale'));
          var reg = parseFloat(btn.getAttribute('data-reg'));
          var vit = parseInt(btn.getAttribute('data-vit'), 10);

          groceryCart.push({ id: id, name: name, sale: sale, reg: reg, vit: vit });
          btn.innerHTML = '✔ CLIPPED IN CART ($' + sale.toFixed(2) + ')';
          btn.style.background = 'rgba(0,255,102,0.3)';
          btn.style.borderColor = '#ffffff';

          updateGroceryCartUI();

          var receiptFeed = document.getElementById('grocery-receipt-feed');
          if (receiptFeed) {
            receiptFeed.innerHTML = '⟦ SCANNER ⟧ Clipped coupon for <strong>' + name + '</strong>. Saved $' + (reg - sale).toFixed(2) + '! Added to cart.';
          }
        });
      });

      // Clear Grocery Cart
      var btnClearCart = document.getElementById('btn-clear-grocery-cart');
      if (btnClearCart) {
        btnClearCart.addEventListener('click', function() {
          groceryCart = [];
          clipBtns.forEach(function(b) {
            var origSale = b.getAttribute('data-sale');
            b.innerHTML = '✂️ CLIP &amp; ADD (+$' + origSale + ')';
            b.style.background = '';
            b.style.borderColor = '';
          });
          updateGroceryCartUI();
          var receiptFeed = document.getElementById('grocery-receipt-feed');
          if (receiptFeed) receiptFeed.innerText = '⟦ CART EMPTIED ⟧ Aisle is clear. Ready to clip fresh weekly deals.';
        });
      }

      // Checkout Button
      var btnCheckout = document.getElementById('btn-checkout-grocery');
      if (btnCheckout) {
        btnCheckout.addEventListener('click', function() {
          if (groceryCart.length === 0) {
            var receiptFeed = document.getElementById('grocery-receipt-feed');
            if (receiptFeed) receiptFeed.innerText = '⚠️ CART IS EMPTY! Clip some weekly deals from the circular flyer first.';
            return;
          }

          var totalSale = 0;
          var totalReg = 0;
          var vitalitySum = 0;
          for (var i = 0; i < groceryCart.length; i++) {
            totalSale += groceryCart[i].sale;
            totalReg += groceryCart[i].reg;
            vitalitySum += groceryCart[i].vit;
          }
          var totalSaved = totalReg - totalSale;

          // Deduct from bank checking
          if (bankState.checking >= totalSale) {
            bankState.checking -= totalSale;
          } else {
            bankState.checking = Math.max(0, bankState.checking - totalSale);
          }
          updateBankUI();

          var receiptFeed = document.getElementById('grocery-receipt-feed');
          if (receiptFeed) {
            receiptFeed.innerHTML = '<span style="color:#00ff66; font-weight:900;">✔ CHECKOUT COMPLETE:</span> Paid $' + totalSale.toFixed(2) + ' with digital coupons applied. <strong>YOU SAVED $' + totalSaved.toFixed(2) + ' (' + Math.round((totalSaved / totalReg) * 100) + '% OFF)!</strong> Body Vitality boosted.';
          }

          // Boost Soul Calculator Body & Mind pillars
          if (window.adjustSoulCalculator) {
            window.adjustSoulCalculator(6, 12, 8, 7);
          }

          // Empty cart after successful checkout
          setTimeout(function() {
            groceryCart = [];
            clipBtns.forEach(function(b) {
              var origSale = b.getAttribute('data-sale');
              b.innerHTML = '✂️ CLIP &amp; ADD (+$' + origSale + ')';
              b.style.background = '';
              b.style.borderColor = '';
            });
            updateGroceryCartUI();
          }, 3500);
        });
      }

      // -----------------------------------------------------------------------
      // LEVEL 03: PHARMACY & UTILITIES ENGINE
      // -----------------------------------------------------------------------
      var btnRx = document.getElementById('btn-fulfill-rx');
      if (btnRx) {
        btnRx.addEventListener('click', function() {
          if (bankState.checking >= 25.0) {
            bankState.checking -= 25.0;
          }
          updateBankUI();

          var feed3 = document.getElementById('level-3-feed');
          if (feed3) {
            feed3.innerHTML = '<span style="color:#00ff66;">✔ RX FULFILLED:</span> Sight prescription drops &amp; cellular phototherapy vitamins received. Cellular nervous vitality +12%.';
          }

          if (window.adjustSoulCalculator) {
            window.adjustSoulCalculator(4, 12, 6, 4);
          }
        });
      }

      var btnUtilities = document.getElementById('btn-negotiate-utilities');
      if (btnUtilities) {
        btnUtilities.addEventListener('click', function() {
          var feed3 = document.getElementById('level-3-feed');
          if (feed3) {
            feed3.innerHTML = '<span style="color:#d500f9;">🤖 AI BILL NEGOTIATOR SUCCESS:</span> Fiber internet &amp; electric rate discounted. Permanent monthly savings: $45.00/mo!';
          }

          if (window.adjustSoulCalculator) {
            window.adjustSoulCalculator(6, 4, 7, 10);
          }
        });
      }

      // Initial UI Sync
      updateBankUI();
      updateGroceryCartUI();
    })();
'''

# Check for existing initRealWorldLevelsEngine to avoid duplicates
if 'initRealWorldLevelsEngine' in home:
    print("WARNING: initRealWorldLevelsEngine already present in homepage.html! Skipping duplicate injection.")
else:
    # Target location: right before `// END SPECTRUM MONOPOLY GAME ENGINE`
    pattern = r'(\s*// END SPECTRUM MONOPOLY GAME ENGINE)'
    match = re.search(pattern, home)
    if not match:
        print("ERROR: Could not find `// END SPECTRUM MONOPOLY GAME ENGINE` in homepage.html!")
        exit(1)
    
    print("Found insertion point before `// END SPECTRUM MONOPOLY GAME ENGINE`.")
    home = home[:match.start()] + '\n' + LEVELS_JS_ENGINE + '\n' + home[match.start():]

# Strict check for WordPress entity safety: zero raw '&&' inside <script> tags
print("Performing strict WordPress entity safety verification (checking for raw '&&')...")
script_blocks = re.findall(r'<script[\s\S]*?</script>', home)
raw_amp_found = False
for i, sb in enumerate(script_blocks):
    if '&&' in sb:
        print(f"CRITICAL ERROR: Found raw '&&' in script block {i}!")
        lines = sb.split('\n')
        for line in lines:
            if '&&' in line:
                print(f"  Line: {line.strip()}")
        raw_amp_found = True

if raw_amp_found:
    print("Aborting write due to raw '&&' in script tags.")
    exit(1)

print("SUCCESS: 0 raw '&&' found in all script blocks! Safe for WordPress.")

with open(HOMEPAGE_PATH, 'w', encoding='utf-8') as f:
    f.write(home)

print(f"Saved updated homepage.html with Real-World Levels Engine. Final size: {len(home)} characters.")
