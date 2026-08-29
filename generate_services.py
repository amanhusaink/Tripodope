import re
import os

source_file = "c:/Users/aman/Desktop/Tripodope/customize-package.html"
dest_file = "c:/Users/aman/Desktop/Tripodope/services.html"

with open(source_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Title and Meta
content = re.sub(
    r'<title>.*?</title>',
    '<title>Our Services - Tripodope</title>',
    content,
    flags=re.DOTALL
)
content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Explore our travel services including custom Europe tours, global getaways, flight tickets, train bookings, and visa services.">',
    content,
    flags=re.DOTALL
)

# 2. Update Hero Section
hero_html = """
  <!-- HERO HEADER SECTION -->
  <section class="bg-gradient-to-b from-[#11223A] to-[#162a45] text-white py-12 md:py-16 relative overflow-hidden">
    <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#C19A58_1px,transparent_1px)] [background-size:16px_16px]"></div>
    <div class="max-w-4xl mx-auto px-4 sm:px-6 text-center relative z-10 space-y-4">
      <div class="inline-flex items-center gap-2 bg-[#C19A58]/20 border border-[#C19A58]/40 px-4 py-1.5 rounded-full text-xs font-bold text-[#C19A58] uppercase tracking-wider">
        <span id="hero-icon">🌍</span> <span id="hero-badge">Tripodope Services</span>
      </div>
      <h1 id="hero-title" class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white tracking-tight transition-all duration-300">
        Our Travel Services
      </h1>
      <p id="hero-subtitle" class="text-sm sm:text-base text-gray-300 max-w-2xl mx-auto transition-all duration-300">
        Select a service below to get started.
      </p>
    </div>
  </section>
"""
content = re.sub(
    r'<!-- HERO HEADER SECTION -->.*?<!-- MAIN CUSTOMIZATION FORM CONTENT -->',
    hero_html + '\n  <!-- MAIN CUSTOMIZATION FORM CONTENT -->',
    content,
    flags=re.DOTALL
)

# 3. Form Content
forms_html = """
  <main class="flex-grow max-w-4xl w-full mx-auto px-4 sm:px-6 py-10 md:py-14">
    
    <!-- Service Selector -->
    <div class="mb-10 text-center" data-aos="fade-up">
        <label class="block text-sm font-bold text-gray-800 mb-3">Select the service you are looking for:</label>
        <div class="inline-block relative w-full sm:w-2/3 md:w-1/2">
            <select id="service-selector" onchange="switchService(this.value)" class="w-full appearance-none bg-white border-2 border-[#C19A58] text-[#11223A] font-bold text-base sm:text-lg rounded-full px-6 py-3.5 pr-10 shadow-md focus:outline-none focus:ring-4 focus:ring-[#C19A58]/20 transition-all cursor-pointer">
                <option value="europe-tours">1. Europe Tours (Tailor-Made)</option>
                <option value="world-tours">2. World Tours</option>
                <option value="flight-ticket">3. Flight Ticket Inquiry</option>
                <option value="train-ticket">4. Train Ticket Booking</option>
                <option value="bus-ticket">5. Bus Ticket Booking</option>
                <option value="visa-services">6. Visa & Passport Services</option>
                <option value="private-transfer">7. Private Transfer</option>
            </select>
            <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-6 text-[#C19A58]">
                <svg class="fill-current h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
            </div>
        </div>
    </div>

    <!-- 1. Europe Tours (Tailor-Made) Form -->
    <form id="form-europe-tours" class="service-form space-y-8" onsubmit="handleEuropeToursSubmit(event)">
      <!-- YOUR TRIP DETAILS -->
      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200/80 space-y-6" data-aos="fade-up">
        <div class="border-b border-gray-100 pb-4">
          <h2 class="text-lg md:text-xl font-bold text-[#11223A]">SECTION 1: YOUR TRIP DETAILS</h2>
        </div>
        <!-- Which European Countries Do You Want to Visit? -->
        <div class="space-y-3">
          <label class="block text-xs sm:text-sm font-bold text-gray-800">
            Which European Countries Do You Want to Visit? <span class="text-gray-400 font-normal">(Multi-Select)</span>
          </label>
          <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-2.5">
            <!-- (Abridged for brevity in script, we will keep just a few popular ones or generate all) -->
            <label class="relative cursor-pointer select-none">
              <input type="checkbox" name="et_countries" value="Austria" class="country-checkbox sr-only">
              <div class="flex items-center justify-between p-3 rounded-xl border border-gray-200 bg-gray-50/60 hover:bg-gray-100/80 transition-all text-xs font-medium text-gray-700">
                <span class="flex items-center gap-2"><img src="https://flagcdn.com/w40/at.png" alt="Austria" class="w-4 h-3 object-cover rounded-[2px]"> Austria</span>
                <span class="check-icon hidden w-4 h-4 rounded-full bg-[#C19A58] text-white items-center justify-center text-[10px]">✓</span>
              </div>
            </label>
            <label class="relative cursor-pointer select-none">
              <input type="checkbox" name="et_countries" value="Belgium" class="country-checkbox sr-only">
              <div class="flex items-center justify-between p-3 rounded-xl border border-gray-200 bg-gray-50/60 hover:bg-gray-100/80 transition-all text-xs font-medium text-gray-700">
                <span class="flex items-center gap-2"><img src="https://flagcdn.com/w40/be.png" alt="Belgium" class="w-4 h-3 object-cover rounded-[2px]"> Belgium</span>
                <span class="check-icon hidden w-4 h-4 rounded-full bg-[#C19A58] text-white items-center justify-center text-[10px]">✓</span>
              </div>
            </label>
            <label class="relative cursor-pointer select-none">
              <input type="checkbox" name="et_countries" value="France" class="country-checkbox sr-only">
              <div class="flex items-center justify-between p-3 rounded-xl border border-gray-200 bg-gray-50/60 hover:bg-gray-100/80 transition-all text-xs font-medium text-gray-700">
                <span class="flex items-center gap-2"><img src="https://flagcdn.com/w40/fr.png" alt="France" class="w-4 h-3 object-cover rounded-[2px]"> France</span>
                <span class="check-icon hidden w-4 h-4 rounded-full bg-[#C19A58] text-white items-center justify-center text-[10px]">✓</span>
              </div>
            </label>
            <label class="relative cursor-pointer select-none">
              <input type="checkbox" name="et_countries" value="Germany" class="country-checkbox sr-only">
              <div class="flex items-center justify-between p-3 rounded-xl border border-gray-200 bg-gray-50/60 hover:bg-gray-100/80 transition-all text-xs font-medium text-gray-700">
                <span class="flex items-center gap-2"><img src="https://flagcdn.com/w40/de.png" alt="Germany" class="w-4 h-3 object-cover rounded-[2px]"> Germany</span>
                <span class="check-icon hidden w-4 h-4 rounded-full bg-[#C19A58] text-white items-center justify-center text-[10px]">✓</span>
              </div>
            </label>
            <label class="relative cursor-pointer select-none">
              <input type="checkbox" name="et_countries" value="Italy" class="country-checkbox sr-only">
              <div class="flex items-center justify-between p-3 rounded-xl border border-gray-200 bg-gray-50/60 hover:bg-gray-100/80 transition-all text-xs font-medium text-gray-700">
                <span class="flex items-center gap-2"><img src="https://flagcdn.com/w40/it.png" alt="Italy" class="w-4 h-3 object-cover rounded-[2px]"> Italy</span>
                <span class="check-icon hidden w-4 h-4 rounded-full bg-[#C19A58] text-white items-center justify-center text-[10px]">✓</span>
              </div>
            </label>
            <label class="relative cursor-pointer select-none">
              <input type="checkbox" name="et_countries" value="Spain" class="country-checkbox sr-only">
              <div class="flex items-center justify-between p-3 rounded-xl border border-gray-200 bg-gray-50/60 hover:bg-gray-100/80 transition-all text-xs font-medium text-gray-700">
                <span class="flex items-center gap-2"><img src="https://flagcdn.com/w40/es.png" alt="Spain" class="w-4 h-3 object-cover rounded-[2px]"> Spain</span>
                <span class="check-icon hidden w-4 h-4 rounded-full bg-[#C19A58] text-white items-center justify-center text-[10px]">✓</span>
              </div>
            </label>
            <label class="relative cursor-pointer select-none">
              <input type="checkbox" name="et_countries" value="Switzerland" class="country-checkbox sr-only">
              <div class="flex items-center justify-between p-3 rounded-xl border border-gray-200 bg-gray-50/60 hover:bg-gray-100/80 transition-all text-xs font-medium text-gray-700">
                <span class="flex items-center gap-2"><img src="https://flagcdn.com/w40/ch.png" alt="Switzerland" class="w-4 h-3 object-cover rounded-[2px]"> Switzerland</span>
                <span class="check-icon hidden w-4 h-4 rounded-full bg-[#C19A58] text-white items-center justify-center text-[10px]">✓</span>
              </div>
            </label>
            <label class="relative cursor-pointer select-none">
              <input type="checkbox" name="et_countries" value="Netherlands" class="country-checkbox sr-only">
              <div class="flex items-center justify-between p-3 rounded-xl border border-gray-200 bg-gray-50/60 hover:bg-gray-100/80 transition-all text-xs font-medium text-gray-700">
                <span class="flex items-center gap-2"><img src="https://flagcdn.com/w40/nl.png" alt="Netherlands" class="w-4 h-3 object-cover rounded-[2px]"> Netherlands</span>
                <span class="check-icon hidden w-4 h-4 rounded-full bg-[#C19A58] text-white items-center justify-center text-[10px]">✓</span>
              </div>
            </label>
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 pt-2">
          <!-- Preferred Departure Dates -->
          <div class="space-y-2">
            <label class="block text-xs sm:text-sm font-bold text-gray-800">Preferred Departure / Travel Dates:</label>
            <input type="date" name="et_departure_date" id="et_departure_date" class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm text-gray-800 focus:outline-none focus:border-[#C19A58]" />
            <label class="inline-flex items-center gap-2 cursor-pointer pt-1">
              <input type="checkbox" id="et_flexible_dates" onchange="document.getElementById('et_departure_date').disabled = this.checked;" class="w-4 h-4 text-[#C19A58] rounded border-gray-300 focus:ring-[#C19A58]">
              <span class="text-xs text-gray-600 font-medium">Flexible dates</span>
            </label>
          </div>
          <!-- Number of Days -->
          <div class="space-y-2">
            <label class="block text-xs sm:text-sm font-bold text-gray-800">Number of Days:</label>
            <input type="number" name="et_num_days" id="et_num_days" min="1" class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm text-gray-800 focus:outline-none focus:border-[#C19A58]" />
            <label class="inline-flex items-center gap-2 cursor-pointer pt-1">
              <input type="checkbox" id="et_flexible_days" onchange="document.getElementById('et_num_days').disabled = this.checked;" class="w-4 h-4 text-[#C19A58] rounded border-gray-300 focus:ring-[#C19A58]">
              <span class="text-xs text-gray-600 font-medium">Flexible days</span>
            </label>
          </div>
        </div>

        <!-- Number of Travelers -->
        <div class="space-y-3 pt-2">
          <label class="block text-xs sm:text-sm font-bold text-gray-800">Number of Travelers:</label>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div class="bg-gray-50/80 p-4 rounded-xl border border-gray-200 flex justify-between">
              <div><span class="block text-xs font-bold text-gray-800">Adults</span><span class="text-[11px] text-gray-500">(12+ yrs)</span></div>
              <input type="number" name="et_adults" value="2" min="1" class="w-16 text-center border border-gray-200 rounded-lg text-sm font-bold text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
            <div class="bg-gray-50/80 p-4 rounded-xl border border-gray-200 flex justify-between">
              <div><span class="block text-xs font-bold text-gray-800">Children</span><span class="text-[11px] text-gray-500">(2–11 yrs)</span></div>
              <input type="number" name="et_children" value="0" min="0" class="w-16 text-center border border-gray-200 rounded-lg text-sm font-bold text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
            <div class="bg-gray-50/80 p-4 rounded-xl border border-gray-200 flex justify-between">
              <div><span class="block text-xs font-bold text-gray-800">Infants</span><span class="text-[11px] text-gray-500">(Under 2 yrs)</span></div>
              <input type="number" name="et_infants" value="0" min="0" class="w-16 text-center border border-gray-200 rounded-lg text-sm font-bold text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
          </div>
        </div>

        <!-- Travel Style -->
        <div class="space-y-3 pt-2">
          <label class="block text-xs sm:text-sm font-bold text-gray-800">Travel Style / Preferences:</label>
          <div class="flex flex-wrap gap-4">
            <label class="inline-flex items-center gap-2 cursor-pointer"><input type="checkbox" name="et_style" value="Private Tours" class="w-4 h-4 text-[#C19A58]"><span class="text-xs font-bold text-gray-800">Private Tours</span></label>
            <label class="inline-flex items-center gap-2 cursor-pointer"><input type="checkbox" name="et_style" value="Train Tours" class="w-4 h-4 text-[#C19A58]"><span class="text-xs font-bold text-gray-800">Train Tours</span></label>
          </div>
        </div>

        <div class="space-y-2 pt-2">
          <label class="block text-xs sm:text-sm font-bold text-gray-800">Tell Us About Your Dream Trip:</label>
          <textarea name="et_dream" rows="3" placeholder="e.g., Specific cities, special occasions..." class="w-full bg-white border border-gray-200 rounded-xl px-4 py-3 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58] resize-none"></textarea>
        </div>
      </div>
      
      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200/80 space-y-6">
        <div class="border-b border-gray-100 pb-4"><h2 class="text-lg md:text-xl font-bold text-[#11223A]">SECTION 2: YOUR CONTACT DETAILS</h2></div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Full Name *</label><input type="text" name="et_name" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Email Address *</label><input type="email" name="et_email" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Phone Number (WhatsApp) *</label><input type="tel" name="et_phone" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Country of Residence *</label><input type="text" name="et_residence" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
        </div>
        <div class="pt-4 text-center">
          <button type="submit" class="w-full sm:w-auto inline-flex items-center justify-center gap-3 bg-[#25D366] hover:bg-[#20bd5a] text-white px-8 py-4 rounded-full font-bold text-sm sm:text-base tracking-wider transition-all shadow-lg hover:-translate-y-0.5">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.105 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-1.157 4.228 4.227-1.157zm11.294-7.227c-.244-.122-1.444-.712-1.668-.794-.224-.081-.388-.122-.551.122-.163.244-.632.794-.775.957-.143.163-.285.183-.529.061-.244-.122-1.033-.381-1.968-1.214-.726-.648-1.216-1.448-1.359-1.693-.143-.244-.015-.376.107-.497.11-.11.244-.285.367-.428.122-.143.163-.244.244-.407.081-.163.041-.306-.02-.428-.061-.122-.551-1.344-.754-1.833-.198-.476-.399-.412-.551-.42h-.469c-.163 0-.428.061-.652.306-.224.244-.856.836-.856 2.039 0 1.203.877 2.364.999 2.527.122.163 1.727 2.637 4.183 3.698.584.252 1.04.403 1.396.516.588.187 1.123.16 1.545.097.471-.07 1.444-.591 1.648-1.161.204-.57.204-1.059.143-1.161-.061-.102-.224-.163-.469-.285z"/></svg>
            SEND REQUEST VIA WHATSAPP
          </button>
        </div>
      </div>
    </form>

    <!-- 2. World Tours Form -->
    <form id="form-world-tours" class="service-form space-y-8 hidden" onsubmit="handleWorldToursSubmit(event)">
      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200/80 space-y-6">
        <div class="border-b border-gray-100 pb-4"><h2 class="text-lg md:text-xl font-bold text-[#11223A]">SECTION 1: YOUR TRIP DETAILS</h2></div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Destination Country / Region:</label><input type="text" name="wt_dest" placeholder="e.g. Kerala, Dubai, Bali..." class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Travel Dates / Month:</label><input type="month" name="wt_date" class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Duration (Days):</label><input type="number" name="wt_days" min="1" class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
        </div>
        <div class="space-y-3 pt-2">
          <label class="block text-xs sm:text-sm font-bold text-gray-800">Number of Travelers:</label>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div class="bg-gray-50/80 p-4 rounded-xl border border-gray-200 flex justify-between">
              <div><span class="block text-xs font-bold text-gray-800">Adults</span></div>
              <input type="number" name="wt_adults" value="2" min="1" class="w-16 text-center border border-gray-200 rounded-lg text-sm font-bold text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
            <div class="bg-gray-50/80 p-4 rounded-xl border border-gray-200 flex justify-between">
              <div><span class="block text-xs font-bold text-gray-800">Children</span></div>
              <input type="number" name="wt_children" value="0" min="0" class="w-16 text-center border border-gray-200 rounded-lg text-sm font-bold text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
            <div class="bg-gray-50/80 p-4 rounded-xl border border-gray-200 flex justify-between">
              <div><span class="block text-xs font-bold text-gray-800">Infants</span></div>
              <input type="number" name="wt_infants" value="0" min="0" class="w-16 text-center border border-gray-200 rounded-lg text-sm font-bold text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
          </div>
        </div>
        <div class="space-y-2 pt-2">
          <label class="block text-xs sm:text-sm font-bold text-gray-800">Special Notes / Requirements:</label>
          <textarea name="wt_notes" rows="3" class="w-full bg-white border border-gray-200 rounded-xl px-4 py-3 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58] resize-none"></textarea>
        </div>
      </div>
      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200/80 space-y-6">
        <div class="border-b border-gray-100 pb-4"><h2 class="text-lg md:text-xl font-bold text-[#11223A]">SECTION 2: YOUR CONTACT DETAILS</h2></div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Full Name *</label><input type="text" name="wt_name" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Email Address *</label><input type="email" name="wt_email" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Phone Number (WhatsApp) *</label><input type="tel" name="wt_phone" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
        </div>
        <div class="pt-4 text-center">
          <button type="submit" class="w-full sm:w-auto inline-flex items-center justify-center gap-3 bg-[#25D366] hover:bg-[#20bd5a] text-white px-8 py-4 rounded-full font-bold text-sm sm:text-base tracking-wider transition-all shadow-lg hover:-translate-y-0.5">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.105 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-1.157 4.228 4.227-1.157zm11.294-7.227c-.244-.122-1.444-.712-1.668-.794-.224-.081-.388-.122-.551.122-.163.244-.632.794-.775.957-.143.163-.285.183-.529.061-.244-.122-1.033-.381-1.968-1.214-.726-.648-1.216-1.448-1.359-1.693-.143-.244-.015-.376.107-.497.11-.11.244-.285.367-.428.122-.143.163-.244.244-.407.081-.163.041-.306-.02-.428-.061-.122-.551-1.344-.754-1.833-.198-.476-.399-.412-.551-.42h-.469c-.163 0-.428.061-.652.306-.224.244-.856.836-.856 2.039 0 1.203.877 2.364.999 2.527.122.163 1.727 2.637 4.183 3.698.584.252 1.04.403 1.396.516.588.187 1.123.16 1.545.097.471-.07 1.444-.591 1.648-1.161.204-.57.204-1.059.143-1.161-.061-.102-.224-.163-.469-.285z"/></svg>
            SEND REQUEST VIA WHATSAPP
          </button>
        </div>
      </div>
    </form>

    <!-- 3. Flight Ticket Inquiry Form -->
    <form id="form-flight-ticket" class="service-form space-y-8 hidden" onsubmit="handleFlightTicketSubmit(event)">
      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200/80 space-y-6">
        <div class="border-b border-gray-100 pb-4"><h2 class="text-lg md:text-xl font-bold text-[#11223A]">SECTION 1: FLIGHT DETAILS</h2></div>
        <div class="space-y-3">
          <label class="block text-xs sm:text-sm font-bold text-gray-800">Trip Type:</label>
          <div class="flex flex-wrap gap-4">
            <label class="inline-flex items-center gap-2"><input type="radio" name="ft_trip_type" value="Round Trip" checked class="w-4 h-4 text-[#C19A58]"><span class="text-sm">Round Trip</span></label>
            <label class="inline-flex items-center gap-2"><input type="radio" name="ft_trip_type" value="One Way" class="w-4 h-4 text-[#C19A58]"><span class="text-sm">One Way</span></label>
            <label class="inline-flex items-center gap-2"><input type="radio" name="ft_trip_type" value="Multi-City" class="w-4 h-4 text-[#C19A58]"><span class="text-sm">Multi-City</span></label>
          </div>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 pt-2">
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Origin (Departure City/Airport):</label><input type="text" name="ft_origin" placeholder="e.g. Milan MXP" class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Destination (Arrival City/Airport):</label><input type="text" name="ft_dest" placeholder="e.g. Cochin COK" class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Departure Date:</label><input type="date" name="ft_dep_date" class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Return Date (if Round Trip):</label><input type="date" name="ft_ret_date" class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
        </div>
        <div class="pt-2">
            <label class="inline-flex items-center gap-2 cursor-pointer"><input type="checkbox" name="ft_flex" value="+/- 1 Week Flexible" class="w-4 h-4 text-[#C19A58]"><span class="text-sm font-medium">Dates Flexibility (+/- 1 Week)</span></label>
        </div>
        <div class="space-y-3 pt-2">
          <label class="block text-xs sm:text-sm font-bold text-gray-800">Number of Passengers:</label>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div class="bg-gray-50/80 p-4 rounded-xl border border-gray-200 flex justify-between">
              <div><span class="block text-xs font-bold text-gray-800">Adults</span></div>
              <input type="number" name="ft_adults" value="1" min="1" class="w-16 text-center border border-gray-200 rounded-lg text-sm font-bold text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
            <div class="bg-gray-50/80 p-4 rounded-xl border border-gray-200 flex justify-between">
              <div><span class="block text-xs font-bold text-gray-800">Children</span></div>
              <input type="number" name="ft_children" value="0" min="0" class="w-16 text-center border border-gray-200 rounded-lg text-sm font-bold text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
            <div class="bg-gray-50/80 p-4 rounded-xl border border-gray-200 flex justify-between">
              <div><span class="block text-xs font-bold text-gray-800">Infants</span></div>
              <input type="number" name="ft_infants" value="0" min="0" class="w-16 text-center border border-gray-200 rounded-lg text-sm font-bold text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
          </div>
        </div>
        <div class="space-y-2 pt-2">
            <label class="block text-xs sm:text-sm font-bold text-gray-800">Cabin Class:</label>
            <select name="ft_cabin" class="w-full sm:w-1/2 bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]">
                <option>Economy</option>
                <option>Premium Economy</option>
                <option>Business Class</option>
            </select>
        </div>
      </div>
      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200/80 space-y-6">
        <div class="border-b border-gray-100 pb-4"><h2 class="text-lg md:text-xl font-bold text-[#11223A]">SECTION 2: YOUR CONTACT DETAILS</h2></div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Full Name *</label><input type="text" name="ft_name" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Email Address *</label><input type="email" name="ft_email" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Phone Number (WhatsApp) *</label><input type="tel" name="ft_phone" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
        </div>
        <div class="pt-4 text-center">
          <button type="submit" class="w-full sm:w-auto inline-flex items-center justify-center gap-3 bg-[#25D366] hover:bg-[#20bd5a] text-white px-8 py-4 rounded-full font-bold text-sm sm:text-base tracking-wider transition-all shadow-lg hover:-translate-y-0.5">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.105 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-1.157 4.228 4.227-1.157zm11.294-7.227c-.244-.122-1.444-.712-1.668-.794-.224-.081-.388-.122-.551.122-.163.244-.632.794-.775.957-.143.163-.285.183-.529.061-.244-.122-1.033-.381-1.968-1.214-.726-.648-1.216-1.448-1.359-1.693-.143-.244-.015-.376.107-.497.11-.11.244-.285.367-.428.122-.143.163-.244.244-.407.081-.163.041-.306-.02-.428-.061-.122-.551-1.344-.754-1.833-.198-.476-.399-.412-.551-.42h-.469c-.163 0-.428.061-.652.306-.224.244-.856.836-.856 2.039 0 1.203.877 2.364.999 2.527.122.163 1.727 2.637 4.183 3.698.584.252 1.04.403 1.396.516.588.187 1.123.16 1.545.097.471-.07 1.444-.591 1.648-1.161.204-.57.204-1.059.143-1.161-.061-.102-.224-.163-.469-.285z"/></svg>
            SEND REQUEST VIA WHATSAPP
          </button>
        </div>
      </div>
    </form>

    <!-- 4. Train Ticket Booking Form -->
    <form id="form-train-ticket" class="service-form space-y-8 hidden" onsubmit="handleTrainTicketSubmit(event)">
      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200/80 space-y-6">
        <div class="border-b border-gray-100 pb-4"><h2 class="text-lg md:text-xl font-bold text-[#11223A]">SECTION 1: JOURNEY DETAILS</h2></div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Departure Station / City:</label><input type="text" name="tt_dep" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Arrival Station / City:</label><input type="text" name="tt_arr" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Travel Date:</label><input type="date" name="tt_date" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
        </div>
        <div class="space-y-3 pt-2">
          <label class="block text-xs sm:text-sm font-bold text-gray-800">Number of Passengers:</label>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
            <div class="bg-gray-50/80 p-3 rounded-xl border border-gray-200 flex flex-col items-center">
              <span class="block text-xs font-bold text-gray-800 mb-2">Adults</span>
              <input type="number" name="tt_adults" value="1" min="0" class="w-full text-center border border-gray-200 rounded-lg text-sm font-bold py-1 text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
            <div class="bg-gray-50/80 p-3 rounded-xl border border-gray-200 flex flex-col items-center">
              <span class="block text-xs font-bold text-gray-800 mb-2">Youth (Under 26)</span>
              <input type="number" name="tt_youth" value="0" min="0" class="w-full text-center border border-gray-200 rounded-lg text-sm font-bold py-1 text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
            <div class="bg-gray-50/80 p-3 rounded-xl border border-gray-200 flex flex-col items-center">
              <span class="block text-xs font-bold text-gray-800 mb-2">Seniors</span>
              <input type="number" name="tt_seniors" value="0" min="0" class="w-full text-center border border-gray-200 rounded-lg text-sm font-bold py-1 text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
            <div class="bg-gray-50/80 p-3 rounded-xl border border-gray-200 flex flex-col items-center">
              <span class="block text-xs font-bold text-gray-800 mb-2">Children</span>
              <input type="number" name="tt_children" value="0" min="0" class="w-full text-center border border-gray-200 rounded-lg text-sm font-bold py-1 text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
          </div>
        </div>
      </div>
      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200/80 space-y-6">
        <div class="border-b border-gray-100 pb-4"><h2 class="text-lg md:text-xl font-bold text-[#11223A]">SECTION 2: YOUR CONTACT DETAILS</h2></div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Full Name *</label><input type="text" name="tt_name" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Phone Number (WhatsApp) *</label><input type="tel" name="tt_phone" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
        </div>
        <div class="pt-4 text-center">
          <button type="submit" class="w-full sm:w-auto inline-flex items-center justify-center gap-3 bg-[#25D366] hover:bg-[#20bd5a] text-white px-8 py-4 rounded-full font-bold text-sm sm:text-base tracking-wider transition-all shadow-lg hover:-translate-y-0.5">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.105 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-1.157 4.228 4.227-1.157zm11.294-7.227c-.244-.122-1.444-.712-1.668-.794-.224-.081-.388-.122-.551.122-.163.244-.632.794-.775.957-.143.163-.285.183-.529.061-.244-.122-1.033-.381-1.968-1.214-.726-.648-1.216-1.448-1.359-1.693-.143-.244-.015-.376.107-.497.11-.11.244-.285.367-.428.122-.143.163-.244.244-.407.081-.163.041-.306-.02-.428-.061-.122-.551-1.344-.754-1.833-.198-.476-.399-.412-.551-.42h-.469c-.163 0-.428.061-.652.306-.224.244-.856.836-.856 2.039 0 1.203.877 2.364.999 2.527.122.163 1.727 2.637 4.183 3.698.584.252 1.04.403 1.396.516.588.187 1.123.16 1.545.097.471-.07 1.444-.591 1.648-1.161.204-.57.204-1.059.143-1.161-.061-.102-.224-.163-.469-.285z"/></svg>
            SEND REQUEST VIA WHATSAPP
          </button>
        </div>
      </div>
    </form>

    <!-- 5. Bus Ticket Booking Form -->
    <form id="form-bus-ticket" class="service-form space-y-8 hidden" onsubmit="handleBusTicketSubmit(event)">
      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200/80 space-y-6">
        <div class="border-b border-gray-100 pb-4"><h2 class="text-lg md:text-xl font-bold text-[#11223A]">SECTION 1: JOURNEY DETAILS</h2></div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">From (City):</label><input type="text" name="bt_dep" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">To (City):</label><input type="text" name="bt_arr" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Travel Date:</label><input type="date" name="bt_date" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Number of Seats:</label><input type="number" name="bt_seats" min="1" value="1" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
        </div>
      </div>
      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200/80 space-y-6">
        <div class="border-b border-gray-100 pb-4"><h2 class="text-lg md:text-xl font-bold text-[#11223A]">SECTION 2: YOUR CONTACT DETAILS</h2></div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Full Name *</label><input type="text" name="bt_name" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Phone Number (WhatsApp) *</label><input type="tel" name="bt_phone" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
        </div>
        <div class="pt-4 text-center">
          <button type="submit" class="w-full sm:w-auto inline-flex items-center justify-center gap-3 bg-[#25D366] hover:bg-[#20bd5a] text-white px-8 py-4 rounded-full font-bold text-sm sm:text-base tracking-wider transition-all shadow-lg hover:-translate-y-0.5">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.105 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-1.157 4.228 4.227-1.157zm11.294-7.227c-.244-.122-1.444-.712-1.668-.794-.224-.081-.388-.122-.551.122-.163.244-.632.794-.775.957-.143.163-.285.183-.529.061-.244-.122-1.033-.381-1.968-1.214-.726-.648-1.216-1.448-1.359-1.693-.143-.244-.015-.376.107-.497.11-.11.244-.285.367-.428.122-.143.163-.244.244-.407.081-.163.041-.306-.02-.428-.061-.122-.551-1.344-.754-1.833-.198-.476-.399-.412-.551-.42h-.469c-.163 0-.428.061-.652.306-.224.244-.856.836-.856 2.039 0 1.203.877 2.364.999 2.527.122.163 1.727 2.637 4.183 3.698.584.252 1.04.403 1.396.516.588.187 1.123.16 1.545.097.471-.07 1.444-.591 1.648-1.161.204-.57.204-1.059.143-1.161-.061-.102-.224-.163-.469-.285z"/></svg>
            SEND REQUEST VIA WHATSAPP
          </button>
        </div>
      </div>
    </form>

    <!-- 6. Visa & Passport Services Form -->
    <form id="form-visa-services" class="service-form space-y-8 hidden" onsubmit="handleVisaServicesSubmit(event)">
      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200/80 space-y-6">
        <div class="border-b border-gray-100 pb-4"><h2 class="text-lg md:text-xl font-bold text-[#11223A]">SECTION 1: SERVICE DETAILS</h2></div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="space-y-2">
            <label class="block text-xs sm:text-sm font-bold text-gray-800">Service Required:</label>
            <select name="vs_service" class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]">
              <option>Visa Services</option>
              <option>Passport Services</option>
            </select>
          </div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Intended Travel Date:</label><input type="date" name="vs_date" class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
        </div>
        <div class="space-y-2 pt-2">
          <label class="block text-xs sm:text-sm font-bold text-gray-800">Tell Us More About Your Query:</label>
          <textarea name="vs_query" rows="3" class="w-full bg-white border border-gray-200 rounded-xl px-4 py-3 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58] resize-none"></textarea>
        </div>
      </div>
      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200/80 space-y-6">
        <div class="border-b border-gray-100 pb-4"><h2 class="text-lg md:text-xl font-bold text-[#11223A]">SECTION 2: YOUR CONTACT DETAILS</h2></div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Full Name *</label><input type="text" name="vs_name" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Email Address *</label><input type="email" name="vs_email" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Phone Number (WhatsApp) *</label><input type="tel" name="vs_phone" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
        </div>
        <div class="pt-4 text-center">
          <button type="submit" class="w-full sm:w-auto inline-flex items-center justify-center gap-3 bg-[#25D366] hover:bg-[#20bd5a] text-white px-8 py-4 rounded-full font-bold text-sm sm:text-base tracking-wider transition-all shadow-lg hover:-translate-y-0.5">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.105 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-1.157 4.228 4.227-1.157zm11.294-7.227c-.244-.122-1.444-.712-1.668-.794-.224-.081-.388-.122-.551.122-.163.244-.632.794-.775.957-.143.163-.285.183-.529.061-.244-.122-1.033-.381-1.968-1.214-.726-.648-1.216-1.448-1.359-1.693-.143-.244-.015-.376.107-.497.11-.11.244-.285.367-.428.122-.143.163-.244.244-.407.081-.163.041-.306-.02-.428-.061-.122-.551-1.344-.754-1.833-.198-.476-.399-.412-.551-.42h-.469c-.163 0-.428.061-.652.306-.224.244-.856.836-.856 2.039 0 1.203.877 2.364.999 2.527.122.163 1.727 2.637 4.183 3.698.584.252 1.04.403 1.396.516.588.187 1.123.16 1.545.097.471-.07 1.444-.591 1.648-1.161.204-.57.204-1.059.143-1.161-.061-.102-.224-.163-.469-.285z"/></svg>
            SEND REQUEST VIA WHATSAPP
          </button>
        </div>
      </div>
    </form>

    <!-- 7. Private Transfer Form -->
    <form id="form-private-transfer" class="service-form space-y-8 hidden" onsubmit="handlePrivateTransferSubmit(event)">
      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200/80 space-y-6">
        <div class="border-b border-gray-100 pb-4"><h2 class="text-lg md:text-xl font-bold text-[#11223A]">SECTION 1: TRANSFER DETAILS</h2></div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Pick-up Location:</label><input type="text" name="pt_pickup" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Drop-off Location:</label><input type="text" name="pt_dropoff" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Transfer Date:</label><input type="date" name="pt_date" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Pick-up Time:</label><input type="time" name="pt_time" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
        </div>
        <div class="space-y-3 pt-2">
          <label class="block text-xs sm:text-sm font-bold text-gray-800">Number of Passengers:</label>
          <div class="grid grid-cols-2 gap-4">
            <div class="bg-gray-50/80 p-3 rounded-xl border border-gray-200 flex flex-col items-center">
              <span class="block text-xs font-bold text-gray-800 mb-2">Adults</span>
              <input type="number" name="pt_adults" value="1" min="1" class="w-full text-center border border-gray-200 rounded-lg text-sm font-bold py-1 text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
            <div class="bg-gray-50/80 p-3 rounded-xl border border-gray-200 flex flex-col items-center">
              <span class="block text-xs font-bold text-gray-800 mb-2">Children</span>
              <input type="number" name="pt_children" value="0" min="0" class="w-full text-center border border-gray-200 rounded-lg text-sm font-bold py-1 text-[#11223A] focus:outline-none focus:border-[#C19A58]">
            </div>
          </div>
        </div>
      </div>
      <div class="bg-white rounded-2xl p-6 sm:p-8 shadow-sm border border-gray-200/80 space-y-6">
        <div class="border-b border-gray-100 pb-4"><h2 class="text-lg md:text-xl font-bold text-[#11223A]">SECTION 2: YOUR CONTACT DETAILS</h2></div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Full Name *</label><input type="text" name="pt_name" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
          <div class="space-y-2"><label class="block text-xs sm:text-sm font-bold text-gray-800">Phone Number (WhatsApp) *</label><input type="tel" name="pt_phone" required class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:border-[#C19A58]" /></div>
        </div>
        <div class="pt-4 text-center">
          <button type="submit" class="w-full sm:w-auto inline-flex items-center justify-center gap-3 bg-[#25D366] hover:bg-[#20bd5a] text-white px-8 py-4 rounded-full font-bold text-sm sm:text-base tracking-wider transition-all shadow-lg hover:-translate-y-0.5">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.105 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-1.157 4.228 4.227-1.157zm11.294-7.227c-.244-.122-1.444-.712-1.668-.794-.224-.081-.388-.122-.551.122-.163.244-.632.794-.775.957-.143.163-.285.183-.529.061-.244-.122-1.033-.381-1.968-1.214-.726-.648-1.216-1.448-1.359-1.693-.143-.244-.015-.376.107-.497.11-.11.244-.285.367-.428.122-.143.163-.244.244-.407.081-.163.041-.306-.02-.428-.061-.122-.551-1.344-.754-1.833-.198-.476-.399-.412-.551-.42h-.469c-.163 0-.428.061-.652.306-.224.244-.856.836-.856 2.039 0 1.203.877 2.364.999 2.527.122.163 1.727 2.637 4.183 3.698.584.252 1.04.403 1.396.516.588.187 1.123.16 1.545.097.471-.07 1.444-.591 1.648-1.161.204-.57.204-1.059.143-1.161-.061-.102-.224-.163-.469-.285z"/></svg>
            SEND REQUEST VIA WHATSAPP
          </button>
        </div>
      </div>
    </form>
  </main>
"""
content = re.sub(
    r'<main.*?</main>',
    forms_html,
    content,
    flags=re.DOTALL
)

# 4. JavaScript Logic
js_code = """
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <script>
    AOS.init({ duration: 800, once: true });

    const servicesMeta = {
      'europe-tours': { icon: '🌍', badge: 'Tailor-Made Europe Tours', title: 'Design Your Dream European Vacation', subtitle: 'Custom private tours crafted by our Europe travel experts' },
      'world-tours': { icon: '🌍', badge: 'World Tours', title: 'Plan Your Global Getaway', subtitle: 'Explore Asia, the Americas, Middle East, and beyond' },
      'flight-ticket': { icon: '✈️', badge: 'Flight Ticket Inquiry', title: 'Get the Best Flight Rates', subtitle: 'Exclusive B2B fares for international long-haul flights' },
      'train-ticket': { icon: '🚆', badge: 'Train Ticket Booking', title: 'Book European & Italian Train Tickets', subtitle: 'Fast-track booking for Frecciarossa, Italo, Rail Europe & more' },
      'bus-ticket': { icon: '🚌', badge: 'Bus Ticket Booking', title: 'Easy European Bus Travel', subtitle: 'Affordable bus ticketing for FlixBus, Itabus, and intercity coaches' },
      'visa-services': { icon: '🛂', badge: 'Visa & Passport Services', title: 'Hassle-Free Visa & Passport Assistance', subtitle: 'Expert guidance for Visas and Passport Processing' },
      'private-transfer': { icon: '🚗', badge: 'Private Transfer Booking', title: 'Seamless Airport & City Transfers', subtitle: 'Book reliable private cars, vans, and limousines' }
    };

    function switchService(serviceId) {
      // Hide all forms
      document.querySelectorAll('.service-form').forEach(form => form.classList.add('hidden'));
      
      // Show selected form
      const selectedForm = document.getElementById('form-' + serviceId);
      if(selectedForm) selectedForm.classList.remove('hidden');

      // Update Hero Section
      const meta = servicesMeta[serviceId];
      if(meta) {
          document.getElementById('hero-icon').innerText = meta.icon;
          document.getElementById('hero-badge').innerText = meta.badge;
          document.getElementById('hero-title').innerText = meta.title;
          document.getElementById('hero-subtitle').innerText = meta.subtitle;
      }
      
      // Update dropdown value in case called from URL param
      document.getElementById('service-selector').value = serviceId;
    }

    // Extract query parameter if coming from a specific package or service
    const urlParams = new URLSearchParams(window.location.search);
    const serviceParam = urlParams.get('service');
    if (serviceParam && servicesMeta[serviceParam]) {
        switchService(serviceParam);
    } else {
        // default
        switchService('europe-tours');
    }

    function openWhatsApp(msg) {
        const waUrl = `https://wa.me/393444440325?text=${encodeURIComponent(msg)}`;
        window.open(waUrl, '_blank');
    }

    function handleEuropeToursSubmit(e) {
      e.preventDefault();
      const form = e.target;
      const countries = Array.from(form.querySelectorAll('input[name="et_countries"]:checked')).map(el => el.value);
      const isFlexibleDate = document.getElementById('et_flexible_dates').checked;
      const date = isFlexibleDate ? 'Flexible Dates' : (form.et_departure_date.value || 'Not specified');
      const isFlexibleDays = document.getElementById('et_flexible_days').checked;
      const days = isFlexibleDays ? 'Flexible Duration' : (form.et_num_days.value ? `${form.et_num_days.value} Days` : 'Not specified');
      const styles = Array.from(form.querySelectorAll('input[name="et_style"]:checked')).map(el => el.value);

      let msg = `🇪🇺 *EUROPE TOURS ENQUIRY*\n`;
      msg += `📍 Countries: ${countries.length > 0 ? countries.join(', ') : 'Flexible'}\n`;
      msg += `📅 Date: ${date} | ⏳ Duration: ${days}\n`;
      msg += `👥 Travelers: ${form.et_adults.value} Adults, ${form.et_children.value} Children, ${form.et_infants.value} Infants\n`;
      msg += `🚗 Style: ${styles.length > 0 ? styles.join(', ') : 'Not specified'}\n`;
      msg += `💭 Notes: ${form.et_dream.value.trim() || 'None'}\n`;
      msg += `----------------------------------------\n`;
      msg += `👤 Name: ${form.et_name.value}\n📧 Email: ${form.et_email.value}\n📱 Phone: ${form.et_phone.value}\n🌍 Residence: ${form.et_residence.value}`;
      openWhatsApp(msg);
    }

    function handleWorldToursSubmit(e) {
      e.preventDefault();
      const form = e.target;
      let msg = `🌍 *WORLD TOURS ENQUIRY*\n`;
      msg += `📍 Destination: ${form.wt_dest.value || 'Not specified'}\n`;
      msg += `📅 Travel Month: ${form.wt_date.value || 'Not specified'} | ⏳ Duration: ${form.wt_days.value || 'Not specified'} Days\n`;
      msg += `👥 Travelers: ${form.wt_adults.value} Adults, ${form.wt_children.value} Children, ${form.wt_infants.value} Infants\n`;
      msg += `💭 Notes: ${form.wt_notes.value.trim() || 'None'}\n`;
      msg += `----------------------------------------\n`;
      msg += `👤 Name: ${form.wt_name.value}\n📧 Email: ${form.wt_email.value}\n📱 Phone: ${form.wt_phone.value}`;
      openWhatsApp(msg);
    }

    function handleFlightTicketSubmit(e) {
      e.preventDefault();
      const form = e.target;
      const tripType = form.querySelector('input[name="ft_trip_type"]:checked').value;
      const flex = form.querySelector('input[name="ft_flex"]').checked ? 'Yes (+/- 1 Week)' : 'No';
      let msg = `✈️ *FLIGHT TICKET INQUIRY*\n`;
      msg += `🔄 Type: ${tripType}\n`;
      msg += `🛫 Origin: ${form.ft_origin.value}\n🛬 Destination: ${form.ft_dest.value}\n`;
      msg += `📅 Departure: ${form.ft_dep_date.value || 'Not specified'}\n`;
      if (tripType === 'Round Trip') msg += `📅 Return: ${form.ft_ret_date.value || 'Not specified'}\n`;
      msg += `📆 Flexible: ${flex}\n`;
      msg += `👥 Passengers: ${form.ft_adults.value} Adults, ${form.ft_children.value} Children, ${form.ft_infants.value} Infants\n`;
      msg += `💺 Class: ${form.ft_cabin.value}\n`;
      msg += `----------------------------------------\n`;
      msg += `👤 Name: ${form.ft_name.value}\n📧 Email: ${form.ft_email.value}\n📱 Phone: ${form.ft_phone.value}`;
      openWhatsApp(msg);
    }

    function handleTrainTicketSubmit(e) {
      e.preventDefault();
      const form = e.target;
      let msg = `🚆 *TRAIN TICKET BOOKING*\n`;
      msg += `🚉 From: ${form.tt_dep.value}\n🚉 To: ${form.tt_arr.value}\n`;
      msg += `📅 Date: ${form.tt_date.value}\n`;
      msg += `👥 Passengers: ${form.tt_adults.value} Adults, ${form.tt_youth.value} Youth, ${form.tt_seniors.value} Seniors, ${form.tt_children.value} Children\n`;
      msg += `----------------------------------------\n`;
      msg += `👤 Name: ${form.tt_name.value}\n📱 Phone: ${form.tt_phone.value}`;
      openWhatsApp(msg);
    }

    function handleBusTicketSubmit(e) {
      e.preventDefault();
      const form = e.target;
      let msg = `🚌 *BUS TICKET BOOKING*\n`;
      msg += `📍 From: ${form.bt_dep.value}\n📍 To: ${form.bt_arr.value}\n`;
      msg += `📅 Date: ${form.bt_date.value}\n`;
      msg += `💺 Seats: ${form.bt_seats.value}\n`;
      msg += `----------------------------------------\n`;
      msg += `👤 Name: ${form.bt_name.value}\n📱 Phone: ${form.bt_phone.value}`;
      openWhatsApp(msg);
    }

    function handleVisaServicesSubmit(e) {
      e.preventDefault();
      const form = e.target;
      let msg = `🛂 *VISA & PASSPORT SERVICES*\n`;
      msg += `📝 Service: ${form.vs_service.value}\n`;
      msg += `📅 Intended Travel Date: ${form.vs_date.value || 'Not specified'}\n`;
      msg += `💭 Query: ${form.vs_query.value.trim() || 'None'}\n`;
      msg += `----------------------------------------\n`;
      msg += `👤 Name: ${form.vs_name.value}\n📧 Email: ${form.vs_email.value}\n📱 Phone: ${form.vs_phone.value}`;
      openWhatsApp(msg);
    }

    function handlePrivateTransferSubmit(e) {
      e.preventDefault();
      const form = e.target;
      let msg = `🚗 *PRIVATE TRANSFER BOOKING*\n`;
      msg += `📍 Pick-up: ${form.pt_pickup.value}\n📍 Drop-off: ${form.pt_dropoff.value}\n`;
      msg += `📅 Date: ${form.pt_date.value}\n⏰ Time: ${form.pt_time.value}\n`;
      msg += `👥 Passengers: ${form.pt_adults.value} Adults, ${form.pt_children.value} Children\n`;
      msg += `----------------------------------------\n`;
      msg += `👤 Name: ${form.pt_name.value}\n📱 Phone: ${form.pt_phone.value}`;
      openWhatsApp(msg);
    }

    // Mobile Menu Toggle
    document.getElementById('mobile-menu-button')?.addEventListener('click', function() {
      const menu = document.getElementById('mobile-menu');
      menu.classList.toggle('hidden');
    });
  </script>
"""
content = re.sub(
    r'<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>.*?</script>',
    js_code,
    content,
    flags=re.DOTALL
)

with open(dest_file, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
