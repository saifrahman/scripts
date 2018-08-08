public void fetchAccountDetails() {
        String accountModelId = createAccount();
        String accountFullName = uriJoiner().join(JewelConstants.CSOB_NAMESPACE, "Account");
        String addressFullName = uriJoiner().join(JewelConstants.CSOB_NAMESPACE, "Address");
        Criteria criteria = Criteria.create(accountFullName).select(accountModelId).childCriteria(addressFullName)
                .childCriteria(JewelConstants.MARKER).fetchAll();

        PaginatedModel resultHolder = _facadeService.execute(criteria);

        assertNotNull(resultHolder);
        List<Model> models = resultHolder.getModels();
        Model account = models.get(0);
        assertNotNull(account);
        assertEquals(accountModelId, account.getModelId());
        EStructuralFeature accountAcctName = account.eClass().getEStructuralFeature("acctName");
        assertEquals("Personal Account", account.eGet(accountAcctName));

        EStructuralFeature acctTypeParameter = account.eClass().getEStructuralFeature("acctType");

        EObject acctType = (EObject) account.eGet(acctTypeParameter);

        EStructuralFeature parameterParamValue = acctType.eClass().getEStructuralFeature("paramValue");
        assertEquals("Wealth", acctType.eGet(parameterParamValue));

        assertEquals(2, account.getAssociationMap().size());

        Model address = account.getAssociationMap().get("AccountAddress").get(0);
        assertNotNull(address);
        EStructuralFeature city = address.eClass().getEStructuralFeature("city");
        assertEquals("Chennai", address.eGet(city));

        Marker marker = (Marker) account.getAssociationMap().get("AccountMarker").get(0);
        assertNotNull(marker);
        assertEquals("Account Marker", marker.getName());
        assertEquals(MarkerType.NOTE, marker.getMarkerType());

    }
