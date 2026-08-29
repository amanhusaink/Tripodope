import re

def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except:
        return
        
    # 1. Remove Field 3
    pattern1 = re.compile(r'<div class="hidden lg:block w-\[1px\] h-10 bg-black/10 shrink-0"></div>\s*<!-- Field 3: When -->[\s\S]*?<input.*?id="booking-when-picker".*?>\s*</div>\s*</div>', re.IGNORECASE)
    html = pattern1.sub('', html)
    
    # 2. Add Modal HTML before WhatsApp button
    modal_html = """
<!-- Quote Modal -->
<div id="quote-modal" class="fixed inset-0 z-[100] hidden items-center justify-center">
  <!-- Backdrop -->
  <div class="absolute inset-0 bg-black/50 backdrop-blur-sm transition-opacity" id="quote-modal-backdrop"></div>
  
  <!-- Modal Content -->
  <div class="relative bg-white rounded-3xl p-6 md:p-8 shadow-2xl w-[90%] max-w-md transform scale-95 opacity-0 transition-all duration-300" id="quote-modal-content">
    <button id="close-quote-modal" class="absolute top-4 right-4 text-gray-400 hover:text-red-500 transition-colors">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
    </button>
    
    <h3 class="text-xl md:text-2xl font-extrabold text-[#11223A] mb-2">Complete Your Request</h3>
    <p class="text-sm text-gray-500 mb-6">Please select when you plan to travel so we can provide an accurate quote.</p>
    
    <div class="space-y-5">
      <div>
        <label class="block text-[11px] uppercase font-bold tracking-wider text-[#11223A] mb-2">When are you thinking?</label>
        <div class="relative">
          <select id="modal-when-select" class="w-full bg-[#FAF9F6] border border-gray-200 text-[#11223A] text-sm rounded-xl px-4 py-3 focus:outline-none focus:border-[#C19A58] appearance-none cursor-pointer">
            <option value="" disabled selected>Select an option</option>
            <option value="Flexible / Not sure yet">Flexible / Not sure yet</option>
            <option value="In 1-3 Months">In 1-3 Months</option>
            <option value="In 3-6 Months">In 3-6 Months</option>
            <option value="More than 6 months">More than 6 months</option>
          </select>
          <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-4 text-gray-500">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path></svg>
          </div>
        </div>
      </div>
      
      <button id="modal-submit-btn" class="w-full bg-[#11223A] hover:bg-[#C19A58] text-white py-3.5 rounded-xl font-bold tracking-wide transition-colors shadow-md flex items-center justify-center gap-2">
        Send Request via WhatsApp
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
      </button>
    </div>
  </div>
</div>
"""
    if 'id="quote-modal"' not in html:
        html = html.replace('<!-- WhatsApp Floating Button -->', modal_html + '\n<!-- WhatsApp Floating Button -->')
        
    # 3. Replace JS logic
    js_pattern = re.compile(r'// Booking Bar widget listener[\s\S]*?\)\(\);', re.IGNORECASE)
    
    new_js = """// Booking Bar widget listener
    (function () {
      const submitBtn = document.getElementById('booking-submit');
      const inquiryInput = document.getElementById('booking-inquiry');
      const fromInput = document.getElementById('booking-from');

      // Custom Dropdown elements
      const trigger = document.getElementById('dropdown-trigger');
      const menu = document.getElementById('dropdown-menu');
      const arrow = document.getElementById('dropdown-arrow-icon');
      const label = document.getElementById('dropdown-selected-label');
      const items = document.querySelectorAll('.dropdown-item');

      if (trigger && menu && arrow && label && items.length > 0) {
        function openMenu() {
          menu.classList.remove('hidden');
          // Let layout compile before animating transition
          setTimeout(() => {
            menu.classList.remove('scale-95', 'opacity-0');
            menu.classList.add('scale-100', 'opacity-100');
          }, 10);
          arrow.classList.add('rotate-180');
        }

        function closeMenu() {
          menu.classList.remove('scale-100', 'opacity-100');
          menu.classList.add('scale-95', 'opacity-0');
          arrow.classList.remove('rotate-180');
          setTimeout(() => {
            menu.classList.add('hidden');
          }, 200);
        }

        trigger.addEventListener('click', (e) => {
          e.stopPropagation();
          const isOpen = !menu.classList.contains('hidden') && menu.classList.contains('opacity-100');
          if (isOpen) {
            closeMenu();
          } else {
            openMenu();
          }
        });

        items.forEach(item => {
          item.addEventListener('click', (e) => {
            e.stopPropagation();
            const val = item.getAttribute('data-value');
            label.textContent = val;
            if (inquiryInput) inquiryInput.value = val;
            
            // Update selected classes
            items.forEach(i => {
              i.classList.remove('text-[#C19A58]', 'bg-[#FAF9F6]', 'font-semibold');
              i.classList.add('font-medium');
            });
            item.classList.add('text-[#C19A58]', 'bg-[#FAF9F6]', 'font-semibold');
            item.classList.remove('font-medium');
            
            closeMenu();
          });
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', () => {
          if (!menu.classList.contains('hidden')) {
            closeMenu();
          }
        });
      }

      const quoteModal = document.getElementById('quote-modal');
      const quoteModalBackdrop = document.getElementById('quote-modal-backdrop');
      const quoteModalContent = document.getElementById('quote-modal-content');
      const closeQuoteModal = document.getElementById('close-quote-modal');
      const modalSubmitBtn = document.getElementById('modal-submit-btn');
      const modalWhenSelect = document.getElementById('modal-when-select');

      function openModal() {
        if (!quoteModal) return;
        quoteModal.classList.remove('hidden');
        quoteModal.classList.add('flex');
        setTimeout(() => {
          quoteModalContent.classList.remove('scale-95', 'opacity-0');
          quoteModalContent.classList.add('scale-100', 'opacity-100');
        }, 10);
      }

      function closeModal() {
        if (!quoteModal) return;
        quoteModalContent.classList.remove('scale-100', 'opacity-100');
        quoteModalContent.classList.add('scale-95', 'opacity-0');
        setTimeout(() => {
          quoteModal.classList.add('hidden');
          quoteModal.classList.remove('flex');
        }, 300);
      }

      if (submitBtn) {
        submitBtn.addEventListener('click', (e) => {
          e.preventDefault();
          openModal();
        });
      }

      if (closeQuoteModal) closeQuoteModal.addEventListener('click', closeModal);
      if (quoteModalBackdrop) quoteModalBackdrop.addEventListener('click', closeModal);

      if (modalSubmitBtn) {
        modalSubmitBtn.addEventListener('click', () => {
          const inquiry = inquiryInput ? inquiryInput.value : '';
          const from = (fromInput && fromInput.value.trim()) ? fromInput.value.trim() : 'anywhere';
          const when = (modalWhenSelect && modalWhenSelect.value) ? modalWhenSelect.value : 'flexible dates';
          
          const phone = '393347553788';
          const text = `Hi Tripodope, I am enquiring about: *${inquiry}*\\nTravelling from: *${from}*\\nWhen: *${when}*`;
          const whatsappUrl = `https://wa.me/${phone}?text=${encodeURIComponent(text)}`;
          
          closeModal();
          window.open(whatsappUrl, '_blank');
        });
      }
    })();"""
    html = js_pattern.sub(new_js, html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Updated {filepath}')

update_file('index.html')
update_file('index-v2.html')
