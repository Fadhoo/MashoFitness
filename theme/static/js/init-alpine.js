function data() {
  return {
    isSideMenuOpen: false,
    toggleSideMenu() {
      this.isSideMenuOpen = !this.isSideMenuOpen;
    },
    closeSideMenu() {
      this.isSideMenuOpen = false;
    },
    isNotificationsMenuOpen: false,
    toggleNotificationsMenu() {
      this.isNotificationsMenuOpen = !this.isNotificationsMenuOpen
      get_all_member_remaining_expiredays()
    },
    closeNotificationsMenu() {
      this.isNotificationsMenuOpen = false;
    },
    // header setting
    isSettingOpen: false,
    toggleSettingMenu() {
      this.isSettingOpen = !this.isSettingOpen;
    },
    closeSettingMenu() {
      this.isSettingOpen = false;
    },
    // header Profile
    isProfileMenuOpen: false,
    toggleProfileMenu() {
      this.isProfileMenuOpen = !this.isProfileMenuOpen;
    },
    closeProfileMenu() {
      this.isProfileMenuOpen = false;
    },
    isGymMemberMenuOpen: false,
    toggleGymMemberMenu() {
      this.isGymMemberMenuOpen = !this.isGymMemberMenuOpen;
    },
    isSettingsMenuOpen: false,
    toggleSettingsMenu() {
      this.isSettingsMenuOpen = !this.isSettingsMenuOpen;
    },
    // futsal
    isFutsalMenuOpen: false,
    toggleFutsalMenu() {
      this.isFutsalMenuOpen = !this.isFutsalMenuOpen;
    },
    // Reports
    isReportsMenuOpen: false,
    toggleReportsMenu() {
      this.isReportsMenuOpen = !this.isReportsMenuOpen;
    },
    // Accountings
    isAccountingMenuOpen: false,
    toggleAccountingMenu() {
      this.isAccountingMenuOpen = !this.isAccountingMenuOpen;
    },
    // Items
    isItemsMenuOpen: false,
    toggleItemsMenu() {
      this.isItemsMenuOpen = !this.isItemsMenuOpen;
    },
    // Orders
    isOrdersMenuOpen: false,
    toggleOrdersMenu() {
      this.isOrdersMenuOpen = !this.isOrdersMenuOpen;
    },
    // Purchases
    isPurchasesMenuOpen: false,
    togglePurchasesMenu() {
      this.isPurchasesMenuOpen = !this.isPurchasesMenuOpen;
    },
    // Sales
    isSalesMenuOpen: false,
    toggleSalesMenu() {
      this.isSalesMenuOpen = !this.isSalesMenuOpen;
    },
    // Modal
    isModalOpen: false,
    trapCleanup: null,
    openModal() {
      this.isModalOpen = true;
      this.trapCleanup = focusTrap(document.querySelector('#modal'));
    },
    closeModal() {
      this.isModalOpen = false;
      this.trapCleanup();
    },

    // Modal
    isUpdateModalOpen: false,
    trapCleanup222: null,
    openUpdateModal(id,call) {
      this.isUpdateModalOpen = true;
      this.trapCleanup222 = focusTrap(document.querySelector('#updateModal'));
      if (call=="non_stock"){
        update_query_call_nonstock(id)
      }
      else if (call=="stock"){
      update_query_call(id)}
      
    },
    closeUpdateModal() {
      this.isUpdateModalOpen = false;
      this.trapCleanup222();
    },
    
    // Product Modal
    isProductModalOpen: false,
    trapCleanup1: null,
    openProductModal() {
      this.isProductModalOpen = true
      this.trapCleanup1 = focusTrap(document.querySelector('#productModal'))
    },
    closeProductModal() {
      this.isProductModalOpen = false
      this.trapCleanup1()
    },

    // Inventory Sub Modal
    isSubModalOpen: false,
    trapCleanup2: null,
    openSubModal() {
      this.isSubModalOpen = true
      this.trapCleanup2 = focusTrap(document.querySelector('#SubModal'))
    },
    closeSubModal() {
      this.isSubModalOpen = false
      this.trapCleanup2()
    },

    // SMS Modal
    isSMSModalOpen: false,
    trapCleanupSMS: null,
    openSMSModal(ids) {
      this.isSMSModalOpen = true
      this.trapCleanupSMS = focusTrap(document.querySelector('#SMSModal'))
      set_member_id(ids)

    },
    closeSMSModal() {
      this.isSMSModalOpen = false
      this.trapCleanupSMS()
    },

    // View Bill Modal
    isViewBillModalOpen: false,
    trapCleanupViewBill: null,
    openViewBillModal(id) {
      
      this.isViewBillModalOpen = true
      this.trapCleanupViewBill = focusTrap(document.querySelector('#ViewBillModal'))
      console.log(id)
      ViewBillCall(id)
    },
    closeViewBillModal() {
      this.isViewBillModalOpen = false
      this.trapCleanupViewBill()
    },

    // View ALL Sms Modal
    isViewAllSmsModalOpen: false,
    trapCleanupViewAllSms: null,
    openViewAllSmsModal() {
        
        this.isViewAllSmsModalOpen = true
        this.trapCleanupViewAllSms = focusTrap(document.querySelector('#ViewAllSmsModal'))
      }
    ,
    closeViewAllSmsModal() {
      this.isViewAllSmsModalOpen = false
      this.trapCleanupViewAllSms()
    },
    
  }
}

function ajax_call(id){
  console.log("row id fetch ",id)
}